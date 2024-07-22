## 安装 Thonny

在这一步中，您将安装Thonny或确保您拥有最新版本。 在这一步中，您将安装Thonny或确保您拥有最新版本。 然后，您将连接到一个 Raspberry Pi Pico，并使用 Shell 运行一些简单的 Python 代码。

## --- collapse ---

title: 树莓派上的 Thonny

---

- Thonny 已经安装在 Raspberry Pi OS 上，但可能需要更新到最新版本
- 打开一个终端窗口，可以通过点击屏幕左上角的图标，或者同时按下Ctrl+Alt+T键
- 在窗口中输入以下内容以更新您的操作系统和 Thonny

```bash
sudo apt update && sudo apt upgrade -y
```

\--- /collapse ---

\--- collapse ---

---

title: 在其他操作系统上安装 Thonny

---

- 在 Windows、macOS 和 Linux 上，您可以安装最新的 Thonny IDE 或更新现有版本
- 在网页浏览器中，打开 [thonny.org](https://thonny.org/)
- 在浏览器窗口的右上角，你会看到 Windows 和 macOS 的下载链接，以及 Linux 的使用说明
- 下载相关文件并运行以安装 Thonny

![从 thonny 网站下载的说明](images/thonny-site.png)

\--- /collapse ---

\--- task ---

从应用程序启动器中打开Thonny。 它看起来像这样：

![Thonny 应用](images/thonny-editor.png)

\--- /task ---

\--- task ---

你可以使用 Thonny 来编写标准的 Python 代码。 在主窗口中输入以下内容，然后点击运行按钮（你会被要求保存文件）。 在主窗口中输入以下内容，然后点击运行按钮（你会被要求保存文件）。

```python3
print('Hello World!')
```

\--- /task ---

你现在可以准备好进行下一步，连接你的 Raspberry Pi Pico了。
