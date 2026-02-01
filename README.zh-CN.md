# Claude Code 项目驱动学习插件

[English](README.md) | [中文](README.zh-CN.md)

一个全面的 Claude Code 插件，通过实践项目帮助你学习编程。这个插件提供了结构化的学习方法：创建学习计划、搭建项目脚手架、追踪进度、获得代码审查 - 所有这些都在你的开发工作流中完成。

## 🎯 这个插件的作用

这个插件将 Claude Code 转变为你的个人学习助手，可以：

1. **创建结构化的学习计划** - 将复杂技能拆解为渐进式阶段
2. **搭建项目脚手架** - 设置项目样板代码并标记清晰的 TODO
3. **追踪你的进度** - 监控你完成了哪些阶段
4. **审查你的代码** - 对你的实现提供详细反馈
5. **指导你的学习** - 提供资源、提示和鼓励

## ✨ 核心特性

- 📚 **项目驱动的学习计划** - 多阶段学习路线图，目标明确
- 🏗️ **自动项目脚手架** - 为 React、Python Flask、原生 JS 等生成样板代码
- 📊 **进度追踪** - 基于 JSON 的进度文件追踪你的学习旅程
- 🔍 **代码审查 Agent** - 根据验收标准自动审查
- 📝 **任务管理** - 清晰的 TASKS.md 文件标记你需要实现的内容
- 🎓 **以学习为中心** - 提供结构但不替你完成工作

## 📦 包含的内容

### Skills（技能）
- **`project-driven-learning`** - 生成全面的学习计划
- **`project-scaffold`** - 使用模板搭建项目结构

### Commands（命令）
- `/project:plan` - 创建新的学习计划
- `/project:scaffold` - 为某个阶段设置项目结构
- `/project:progress` - 查看你的学习进度
- `/project:complete` - 标记一个阶段为已完成
- `/project:review` - 请求审查你的实现代码

### Agents（智能代理）
- **`review.md`** - 智能代码审查 agent，验证实现

### Templates（模板）
预构建的项目模板：
- React（使用 Vite）
- Python Flask
- 原生 JavaScript/HTML/CSS

## 🚀 快速开始

### 1. 创建学习计划

```bash
/project:plan 我想通过构建 Todo 应用来学习 React
```

这将会：
- 询问你的经验水平
- 生成多阶段学习计划
- 保存到 `./docs/plans/{日期}-{项目}/plan.md`
- 在 `progress.json` 中初始化进度追踪

### 2. 开始第一阶段

```bash
/project:scaffold
```

这将会：
- 读取你的学习计划
- 检测技术栈
- 在 `./projects/{项目名}/` 创建项目结构
- 生成带有 TODO 标记的样板代码
- 创建 TASKS.md 实现清单

### 3. 实现代码

完成标记在以下位置的任务：
- 带有 `TODO` 和 `USER IMPLEMENTATION REQUIRED` 注释的文件
- `TASKS.md` 清单

### 4. 查看进度（可选）

```bash
/project:progress
```

查看哪些阶段已完成、正在进行或未开始。

### 5. 请求代码审查

```bash
/project:review
```

审查 agent 将会：
- 根据验收标准检查你的实现
- 分析代码质量
- 提供详细反馈
- 保存审查报告到 `./docs/plans/{项目}/reviews/`

### 6. 标记阶段完成

```bash
/project:complete
```

这会更新你的进度，并可选择搭建下一阶段。

### 7. 继续下一阶段

```bash
/project:scaffold stage 2
```

为每个学习阶段重复步骤 3-7！

## 📁 目录结构

使用这个插件后，你的项目将如下所示：

```
你的项目/
├── docs/
│   └── plans/
│       └── 2026-02-02-react-todo-app/
│           ├── plan.md                 # 学习计划
│           ├── progress.json           # 进度追踪
│           └── reviews/                # 代码审查报告
│               ├── stage-1-review.md
│               └── stage-2-review.md
├── projects/
│   └── react-todo-app/                 # 你的实际项目
│       ├── TASKS.md                    # 需要实现的内容
│       ├── README.md                   # 设置说明
│       ├── package.json                # 依赖
│       └── src/
│           ├── App.jsx                 # 你的实现
│           └── ...
├── .claude-plugin/
│   └── plugin.json                     # 插件元数据
├── commands/                           # 命令定义
│   ├── plan.md
│   ├── scaffold.md
│   ├── progress.md
│   ├── complete.md
│   └── review.md
├── agents/
│   └── review.md                       # 审查 agent
└── skills/
    ├── project-driven-learning/
    └── project-scaffold/
```

## 🎓 学习工作流示例

假设你想学习 React：

### 步骤 1：规划
```
你: /project:plan 我想通过构建 Todo 应用来学习 React

Claude: 我会帮你创建学习计划！让我问几个问题...
        [创建结构化的 5 阶段学习计划]

        ✅ 计划已保存到: ./docs/plans/2026-02-02-react-todo-app/plan.md
```

### 步骤 2：搭建
```
你: /project:scaffold

Claude: ✅ 项目脚手架搭建成功！
        位置: ./projects/react-todo-app/
        技术栈: React + Vite
        阶段: 1 - 设置和基础组件

        下一步:
        1. cd projects/react-todo-app
        2. npm install
        3. 查看 TASKS.md
        4. npm run dev
```

### 步骤 3：实现
```
你: [完成代码工作，实现 TODO 项目]
```

### 步骤 4：审查
```
你: /project:review

Claude: # 阶段 1 审查报告

        📊 总体评估: ✅ 通过
        完成度评分: 8.5/10

        ✅ 验收标准审查
        1. ✅ 基础组件结构已创建
        2. ✅ 状态管理已实现
        3. ⚠️ 事件处理器工作正常但可以优化

        [详细反馈和建议]

        🎯 下一步: 准备继续！
        运行 /project:complete 标记此阶段完成。
```

### 步骤 5：完成并继续
```
你: /project:complete

Claude: 🎉 恭喜！阶段 1 已完成！
        进度: 5 个阶段中完成了 1 个（20%）
        准备好进入阶段 2 了吗？

你: /project:scaffold stage 2

Claude: [为阶段 2 设置结构]
```

## 🛠️ 支持的技术

当前包含以下模板：

- **前端**
  - React（使用 Vite）
  - Vue.js
  - 原生 JavaScript/HTML/CSS

- **后端**
  - Python Flask
  - Node.js/Express
  - Python FastAPI

- **移动端**
  - React Native

- **CLI 工具**
  - Python CLI
  - Node.js CLI

没看到你的技术栈？插件仍然可以基于最佳实践创建自定义结构！

## 📋 进度追踪

`progress.json` 文件追踪你的学习旅程：

```json
{
  "project_name": "react-todo-app",
  "project_path": "./projects/react-todo-app",
  "current_stage": 2,
  "total_stages": 5,
  "stages": [
    {
      "stage_number": 1,
      "stage_name": "设置和基础组件",
      "status": "completed",
      "started_at": "2026-02-02T10:00:00Z",
      "completed_at": "2026-02-02T14:30:00Z"
    },
    {
      "stage_number": 2,
      "stage_name": "状态管理",
      "status": "in_progress",
      "started_at": "2026-02-02T15:00:00Z",
      "completed_at": null
    }
  ]
}
```

## 🤖 代码审查功能

审查 agent 提供：

- **验收标准验证** - 检查是否满足所有要求
- **代码质量评估** - 评估结构、命名、组织
- **学习目标检查** - 验证你是否理解了概念
- **建设性反馈** - 具体的、可操作的建议
- **Bug 检测** - 识别常见问题和错误
- **最佳实践** - 突出好的模式和反模式
- **下一步指导** - 明确指导是继续还是改进

## 💡 最佳实践

1. **先阅读计划** - 在开始前了解完整的学习旅程
2. **一次一个阶段** - 不要匆忙完成各个阶段
3. **完成前先审查** - 使用 `/project:review` 验证你的工作
4. **超越要求去实验** - TODO 只是最低要求，多多探索！
5. **保持代码有序** - 遵循脚手架提供的结构
6. **定期检查进度** - 使用 `/project:progress` 保持动力

## 🔧 自定义

### 添加新模板

在 `skills/project-scaffold/assets/templates/{技术栈}/` 中添加模板：

```
templates/
└── 你的技术/
    ├── package.json
    ├── README.md
    └── src/
        └── main.js
```

在 `references/tech_stacks.md` 中更新脚手架指南。

### 修改命令

编辑 `commands/` 中的文件以改变命令行为或添加新命令。

### 自定义审查标准

编辑 `agents/review.md` 以调整审查标准或添加特定技术的检查。

## 📚 示例项目

这个插件可以帮助你通过构建以下项目来学习：

- **React Todo 应用** - 学习组件、状态、事件
- **Python Flask API** - 学习路由、请求处理、JSON 响应
- **原生 JS 计算器** - 学习 DOM 操作、事件处理
- **React 天气仪表板** - 学习 API 集成、async/await
- **Python CLI 工具** - 学习参数解析、文件 I/O
- **Express REST API** - 学习 CRUD 操作、中间件

## ❓ 常见问题

**问：这会帮我写代码吗？**
答：不会！它提供结构、样板代码和 TODO。你需要实现逻辑来学习。

**问：我可以用它学习高级主题吗？**
答：可以！为任何复杂度级别创建计划 - 插件会适应你的目标。

**问：如果我的技术栈不被支持怎么办？**
答：插件仍然可以按照最佳实践创建结构。你也可以添加自定义模板。

**问：我可以跳过阶段吗？**
答：对于学习来说不推荐，但你可以直接搭建任何阶段号。

**问：审查 agent 严格吗？**
答：它以学习为重点：建设性的、教育性的，鼓励成长而非追求完美。

**问：我可以用它进行团队学习吗？**
答：可以！进度文件可以被分享并由导师或同伴审查。

## 🤝 贡献

有改进的想法吗？
- 添加新的技术模板
- 改进审查标准
- 增强命令功能
- 分享示例学习计划

## 📄 许可证

本插件按原样提供，用于教育目的。

## 🎉 学习愉快！

记住：目标不是快速完成 - 而是通过实践**深入学习**。慢慢来，多实验，享受这个过程！

---

**适用于:** Claude Code
**版本:** 1.0.0
**作者:** l1ax
