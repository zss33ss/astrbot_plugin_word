import traceback

from astrbot.api.event import filter, AstrMessageEvent
from astrbot.api.star import Context, Star, register
from astrbot.api import logger

STYLE_MARKER = "<!-- bubbly_barto_style_v1 -->"


@register("bubbly_barto", "zss33ss", "注入说话风格指令，让机器人用简短自然的方式回复", "1.0.0")
class BubblyBarto(Star):
    def __init__(self, context: Context, config: dict | None = None):
        super().__init__(context, config)
        self.config = config or {}

    @filter.on_llm_request()
    async def on_llm_request(self, event: AstrMessageEvent, req) -> None:
        """在 LLM 请求前注入说话风格约束"""
        try:
            if not self.config.get("enable", True):
                return

            if STYLE_MARKER in (req.system_prompt or ""):
                return

            style_prompt = self.config.get(
                "style_prompt",
                "【说话风格要求】\n请用简短、自然的方式回复，像真人聊天一样。",
            )

            max_chars = self.config.get("max_total_chars", 500)
            max_msgs = self.config.get("max_message_count", 3)

            limits = (
                f"\n- 每次回复总字数不超过 {max_chars} 字"
                f"\n- 每次回复不要超过 {max_msgs} 条消息"
            )

            req.system_prompt = (
                (req.system_prompt or "")
                + f"\n\n{style_prompt}\n{limits}\n{STYLE_MARKER}"
            )

        except Exception:
            logger.error(f"[气泡说话] 注入说话风格失败: {traceback.format_exc()}")
