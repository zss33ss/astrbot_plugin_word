# 气泡说话 (BubblyBarto)

让机器人说话更自然——通过在 LLM 请求前注入说话风格指令，从源头约束模型用简短、口语化的方式回复，告别"文字墙"。

## 功能

- 自动在每次 LLM 请求的 system prompt 中追加说话风格约束
- 后台可随时开关，`style_prompt` 支持自定义
- 不影响其他插件，兼容世界书、上下文感知等同样修改 system prompt 的插件

## 配置

在 AstrBot 管理后台的插件配置页可调整：

| 配置项 | 默认值 | 说明 |
|---|---|---|
| `enable` | `true` | 是否启用 |
| `style_prompt` | （见下方） | 自定义说话风格指令 |

**默认 `style_prompt`：**

```
【说话风格要求】
请用简短、自然的方式回复，像真人聊天一样：
- 每条消息控制在 2-3 句话以内，不要输出大段文字
- 直接说重点，不需要客套话
- 用口语化的表达，不要写小作文
- 如果内容确实很多，挑最重要的说
```

## 安装

插件商店搜索"气泡说话"，或手动克隆到 `data/plugins/`：

```bash
git clone https://github.com/zss33ss/astrbot_plugin_word.git data/plugins/astrbot_plugin_word
```

## 原理

通过 `@filter.on_llm_request()` 钩子，在 LLM 请求发出前将 `style_prompt` 追加到 `req.system_prompt` 末尾，附带防重复注入标记。

## 支持

- [AstrBot](https://github.com/AstrBotDevs/AstrBot)
- [AstrBot 插件开发文档](https://docs.astrbot.app/dev/star/plugin-new.html)
