# Skills

个人 Agent skills 集合。每个 skill 独立存放，保留来源，按统一格式维护。

## 目录

| Skill | 用途 |
| --- | --- |
| [frontend-design-references](skills/frontend-design-references/SKILL.md) | 前端设计参考选择、参考说明与动效组件选型 |

## 结构

```text
skills/<skill-name>/
  SKILL.md          # 必需：元信息、触发条件与工作流
  scripts/          # 可选：辅助脚本
  references/       # 可选：详细参考资料
  assets/           # 可选：模板与静态资源
```

## 安装到 Codex

把所需 skill 目录复制到 `~/.codex/skills/`，例如：

```sh
git clone https://github.com/Tsukumi233/skills.git
mkdir -p ~/.codex/skills
cp -R skills/skills/frontend-design-references ~/.codex/skills/
```

如果已安装同名 skill，请先检查差异再更新。安装后在下一轮对话中使用。

## 维护

新增和更新约定见 [CONTRIBUTING.md](CONTRIBUTING.md)。提交前运行：

```sh
python3 scripts/validate_skills.py
```

## 来源与授权

各 skill 在正文或独立来源文件中记录来源。当前 `frontend-design-references` 导入自用户提供的同名 `.skill` 包，正文注明整理自埃弗里特鱼《存 25 个 Vibe Coding 的参考网站》。本仓库未附统一许可证；第三方内容和所引用组件按各自授权使用。
