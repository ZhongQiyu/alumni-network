// index.js

Page({
  data: {
    userInfo: {
      avatarUrl: '/path/to/avatar.png', // 默认头像路径
      nickName: '昵称' // 默认昵称
    },
    wxData: '',
    feishuData: '',
    showForm: false
  },
  login() {
    wx.showToast({
      title: '登录功能待实现',
      icon: 'none'
    });
  },
  getCard() {
    this.setData({
      showForm: true
    });
  },
  onSubmit(e) {
    wx.showToast({
      title: '表单提交成功',
      icon: 'success'
    });
    this.setData({
      showForm: false
    });
  },
  fetchDataFromWx() {
    // 模拟获取微信数据
    this.setData({
      wxData: '微信数据'
    });
  },
  fetchDataFromFeishu() {
    // 模拟获取飞书数据
    this.setData({
      feishuData: '飞书数据'
    });
  }
});
