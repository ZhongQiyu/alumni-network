# mini_program.py

import os
import zipfile

# Define file structure and content
files = {
    "app.js": """
App({
  onLaunch: function () {
    // 展示本地存储能力
    var logs = wx.getStorageSync('logs') || []
    logs.unshift(Date.now())
    wx.setStorageSync('logs', logs)

    // 登录
    wx.login({
      success: res => {
        // 发送 res.code 到后台换取 openId, sessionKey, unionId
        console.log('微信登录成功', res)
        // 假设获取到了 openId
        this.globalData.openId = res.code
      }
    })

    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          // 已经授权，可以直接调用 getUserInfo 获取头像昵称，不会弹框
          wx.getUserInfo({
            success: res => {
              // 可以将 res 发送给后台解码出 unionId
              this.globalData.userInfo = res.userInfo

              // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
              // 所以此处加入 callback 以防止这种情况
              if (this.userInfoReadyCallback) {
                this.userInfoReadyCallback(res)
              }
            }
          })
        }
      }
    })
  },

  onShow: function (options) {
    console.log('小程序显示', options)
  },

  onHide: function () {
    console.log('小程序隐藏')
  },

  onError: function (msg) {
    console.error('小程序错误', msg)
  },

  globalData: {
    userInfo: null,
    openId: null
  },

  requestWx: function (url, method, data, success, fail) {
    wx.request({
      url: url,
      method: method,
      data: data,
      header: {
        'content-type': 'application/json'
      },
      success: function (res) {
        if (res.statusCode == 200) {
          success(res.data)
        } else {
          fail(res)
        }
      },
      fail: function (err) {
        fail(err)
      }
    })
  },

  requestFeishu: function (url, method, data, success, fail) {
    wx.request({
      url: url,
      method: method,
      data: data,
      header: {
        'Content-Type': 'application/json',
        'Authorization': 'Bearer YOUR_FEISHU_ACCESS_TOKEN'
      },
      success: function (res) {
        if (res.statusCode == 200) {
          success(res.data)
        } else {
          fail(res)
        }
      },
      fail: function (err) {
        fail(err)
      }
    })
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
.container {
  padding: 20px;
}
""",
    "project.config.json": """
{
  "pages": [
    "pages/index/index"
  ],
  "window": {
    "backgroundTextStyle": "light",
    "navigationBarBackgroundColor": "#ffffff",
    "navigationBarTitleText": "巴布森校友+",
    "navigationBarTextStyle": "black"
  },
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
""",
    "sitemap.json": """
{
  "rules": [
    {
      "action": "allow",
      "page": "*"
    }
  ]
}
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
