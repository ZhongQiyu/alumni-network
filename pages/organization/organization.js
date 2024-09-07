// organization.js

Page({
  data: {
    organizationInfo: {
      name: "巴布森学院",
      description: "巴布森学院是全球知名的创业教育领袖，致力于培养具备创业精神和技能的未来领导者。",
      logoUrl: "/images/babson_logo.png" // 假设你在 images 文件夹中有这个 logo
    }
  },

  onLoad() {
    // 页面加载时的逻辑，可以从后端获取组织信息
    this.loadOrganizationInfo();
  },

  loadOrganizationInfo() {
    // 模拟从后端获取数据
    wx.request({
      url: 'https://your-backend-api-url/organization', // 替换为实际的后端API地址
      method: 'GET',
      success: (res) => {
        // 假设返回的结果包含组织信息
        this.setData({
          organizationInfo: res.data
        });
      },
      fail: (err) => {
        console.error('获取组织信息失败:', err);
        wx.showToast({
          title: '加载失败，请稍后再试',
          icon: 'error'
        });
      }
    });
  }
});
