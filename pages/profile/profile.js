// pages/profile/profile.js

Page({
  data: {
    logs: [],
    fileStructure: [],
    showForm: false,  // 确保 showForm 被初始化
    userInfo: {}
  },

  onLoad() {
    // 在页面加载时获取用户信息，并加载日志和文件结构
    this.setData({
      userInfo: {
        name: "点击登录账号",
        contact: "XXXXXXXXXXXXXXXX"
      }
    });

    // 页面加载时调用日志和文件结构加载函数
    this.loadLogs();
    this.loadFileStructure();
  },

  login() {
    console.log("点击登录");

    // 登录逻辑
    wx.showToast({
      title: '登录成功',
      icon: 'success'
    });

    // 这里可以进一步实现实际的登录接口调用逻辑
    // wx.request({
    //   url: 'https://your-backend-api-url/login',
    //   method: 'POST',
    //   data: loginData,
    //   success: (res) => {
    //     // 登录成功处理逻辑
    //   },
    //   fail: (err) => {
    //     // 登录失败处理逻辑
    //   }
    // });
  },

  getCard() {
    this.setData({
      showForm: true
    });

    // 处理领取校友卡的逻辑
    wx.showToast({
      title: '领取校友卡功能待实现',
      icon: 'success'
    });

    // 这里可以进一步实现领取校友卡的接口调用逻辑
    // wx.request({
    //   url: 'https://your-backend-api-url/get-card',
    //   method: 'POST',
    //   data: cardData,
    //   success: (res) => {
    //     // 领取成功处理逻辑
    //   },
    //   fail: (err) => {
    //     // 领取失败处理逻辑
    //   }
    // });
  },

  submitForm(e) {
    const formData = e.detail.value;
    console.log('提交的表单数据：', formData);
    
    // 调用服务器API提交表单
    wx.request({
      url: 'https://your-backend-api-url/submit',
      method: 'POST',
      data: formData,
      success(res) {
        wx.showToast({
          title: '表单提交成功',
          icon: 'success'
        });
      },
      fail(err) {
        wx.showToast({
          title: '表单提交失败',
          icon: 'error'
        });
      }
    });

    this.setData({
      showForm: false
    });
  },

  logout() {
    // 退出登录逻辑
    wx.showToast({
      title: '已退出登录',
      icon: 'success'
    });
    // 清除用户数据，返回首页或登录页
    this.setData({
      userInfo: {},
      showForm: false
    });
  },

  loadLogs() {
    wx.request({
      url: 'https://your-backend-api-url/logs',
      success: (res) => {
        this.setData({
          logs: res.data.logs
        });
      },
      fail: (err) => {
        wx.showToast({
          title: '获取日志失败',
          icon: 'error'
        });
      }
    });
  },

  loadFileStructure() {
    wx.request({
      url: 'https://your-backend-api-url/file-structure',
      success: (res) => {
        this.setData({
          fileStructure: res.data.fileStructure
        });
      },
      fail: (err) => {
        wx.showToast({
          title: '获取文件结构失败',
          icon: 'error'
        });
      }
    });
  },

  applyForCard() {
    // 申请校友卡逻辑
    wx.showToast({
      title: '申请成功',
      icon: 'success'
    });

    // 这里可以进一步实现实际的申请接口调用逻辑
    // wx.request({
    //   url: 'https://your-backend-api-url/apply-for-card',
    //   method: 'POST',
    //   data: applicationData,
    //   success: (res) => {
    //     // 申请成功处理逻辑
    //   },
    //   fail: (err) => {
    //     // 申请失败处理逻辑
    //   }
    // });
  }
});
