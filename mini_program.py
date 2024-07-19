import os
import zipfile

# Define file structure and content
files = {
    "app.js": """
App({
  onLaunch: function () {
    // 小程序初始化逻辑
  }
})
""",
    "pages/index/index.js": """
Page({
  data: {
    info: null
  },

  onLoad: function () {
    this.getDataFromServer(this.handleServerResponse);
  },

  // 获取服务器数据的方法
  getDataFromServer: function (callback) {
    wx.request({
      url: 'https://example.com/api/data',
      method: 'GET',
      success: function (res) {
        if (callback) {
          callback(res.data);
        }
      },
      fail: function (err) {
        console.error('请求失败', err);
      }
    });
  },

  // 处理服务器响应的回调函数
  handleServerResponse: function (data) {
    this.setData({
      info: data
    });
  }
})
""",
    "pages/index/index.wxml": """
<view class="container">
  <text>{{info}}</text>
</view>
""",
    "pages/index/index.wxss": """
/* 样式文件 */
.container {
  padding: 20px;
}
""",
    "project.config.json": """
{
  "miniprogramRoot": "./",
  "projectname": "BabsonAlumni",
  "description": "巴布森校友会小程序",
  "appid": "your-app-id",
  "setting": {
    "urlCheck": false,
    "es6": true,
    "enhance": true
  }
}
""",
    "LICENSE": """
MIT License

Permission is hereby granted, free of charge, to any person obtaining a copy
of this software and associated documentation files (the "Software"), to deal
in the Software without restriction, including without limitation the rights
to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
copies of the Software, and to permit persons to whom the Software is
furnished to do so, subject to the following conditions:

The above copyright notice and this permission notice shall be included in all
copies or substantial portions of the Software.

THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
SOFTWARE.
"""
}

# Create directories
os.makedirs("mini_program_project/pages/index", exist_ok=True)

# Save files
for file_path, content in files.items():
    full_path = os.path.join("mini_program_project", file_path)
    with open(full_path, "w") as file:
        file.write(content.strip())

# Zip the project folder
with zipfile.ZipFile("mini_program_project.zip", 'w') as zipf:
    for root, _, files in os.walk("mini_program_project"):
        for file in files:
            zipf.write(os.path.join(root, file))
