// index.js

const app = getApp()

Page({
  data: {
    userInfo: {},
    wxData: null,
    feishuData: null
  },

  onLoad: function () {
    // 获取全局数据
    if (app.globalData.userInfo) {
      this.setData({
        userInfo: app.globalData.userInfo
      })
    } else {
      // 由于 getUserInfo 是网络请求，可能会在 Page.onLoad 之后才返回
      // 所以此处加入 callback 以防止这种情况
      app.userInfoReadyCallback = res => {
        this.setData({
          userInfo: res.userInfo
        })
      }
    }
  },

  // 示例微信网络请求
  fetchDataFromWx: function () {
    app.requestWx('https://example.com/api/data', 'GET', {}, 
      data => {
        this.setData({ wxData: data })
        console.log('微信请求成功', data)
      }, 
      err => {
        console.error('微信请求失败', err)
      }
    )
  },

  // 示例飞书网络请求
  fetchDataFromFeishu: function () {
    app.requestFeishu('https://open.feishu.cn/api/v1/data', 'GET', {}, 
      data => {
        this.setData({ feishuData: data })
        console.log('飞书请求成功', data)
      }, 
      err => {
        console.error('飞书请求失败', err)
      }
    )
  }
})
