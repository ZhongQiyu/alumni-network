// index.js

Page({
  data: {
    userInfo: {
      avatarUrl: 'database/babsonalum.png', // 默认头像路径
      nickName: '昵称' // 默认昵称
    },
    wxData: '', // 微信数据
    feishuData: '', // 飞书数据
    showForm: false // 控制表单显示
  },

  onLoad: function() {
    // 在页面加载时获取一些数据
    this.fetchDataFromWx();
    this.fetchDataFromFeishu();

    // 加载用户信息
    this.setData({
      userInfo: {
        avatarUrl: 'database/babsonalum.png', // 替换为实际的头像路径
        nickName: '默认昵称' // 替换为实际的用户昵称
      }
    });
  },

  login() {
    wx.showToast({
      title: '登录功能待实现',
      icon: 'none'
    });
  },

  getCard() {
    wx.showToast({
      title: '领取成功',
      icon: 'success'
    });
    this.setData({
      showForm: true
    });
  },

  onSubmit(e) {
    const formData = e.detail.value;
    console.log('提交的表单数据：', formData);

    wx.request({
      url: 'https://your-backend-api-url/submit', // 替换为你的后端API地址
      method: 'POST',
      data: formData,
      success: function(res) {
        wx.showToast({
          title: '表单提交成功',
          icon: 'success'
        });
        this.setData({
          showForm: false
        });
      }.bind(this),
      fail: function(err) {
        wx.showToast({
          title: '提交失败',
          icon: 'error'
        });
        console.error('表单提交失败：', err);
      }
    });
  },

  fetchDataFromWx() {
    // 模拟获取微信数据
    this.setData({
      wxData: '微信数据' // 这里可以替换为实际的获取微信数据的逻辑
    });
  },

  fetchDataFromFeishu() {
    // 模拟获取飞书数据
    this.setData({
      feishuData: '飞书数据' // 这里可以替换为实际的获取飞书数据的逻辑
    });
  },

  navigateToHome() {
    wx.navigateTo({
      url: '/pages/index/index'
    });
  },

  navigateToOrganization() {
    wx.navigateTo({
      url: '/pages/organization/organization'
    });
  },
  
  navigateToProfile() {
    wx.navigateTo({
      url: '/pages/profile/profile'
    });
  }
});
