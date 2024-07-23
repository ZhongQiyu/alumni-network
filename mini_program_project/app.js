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