// app.js

App({
  globalData: {
    userInfo: null
  },

  onLaunch: function () {
    // 获取用户信息
    wx.getSetting({
      success: res => {
        if (res.authSetting['scope.userInfo']) {
          wx.getUserInfo({
            success: res => {
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

  requestWx: function (url, method, data, success, fail) {
    wx.request({
      url: url,
      method: method,
      data: data,
      success: success,
      fail: fail
    })
  },

  requestFeishu: function (url, method, data, success, fail) {
    wx.request({
      url: url,
      method: method,
      data: data,
      success: success,
      fail: fail
    })
  }
})
