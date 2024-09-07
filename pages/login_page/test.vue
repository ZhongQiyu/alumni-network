<template>
  <div id="app">
    <!-- ECharts 图表容器 -->
    <div ref="chart" style="width: 100%; height: 1000px;"></div>
  </div>
</template>

<script>
import * as echarts from 'echarts'; // 引入 ECharts 库

export default {
  name: 'App',
  data() {
    return {
      highlightedNode: "课程要求", // 当前高亮的节点，初始为根节点
      allNodes: [
        // 定义所有节点的信息
        // Level 0: 基础知识节点
        { name: '课程要求', level: 0 },
        { name: '学习要点', level: 0 },
        { name: '模式识别预备知识', level: 0 },
        { name: '模式识别相关学科',  level: 0 },
        { name: '模式识别相关教材', level: 0 },
        // Level 1: 进阶知识节点
        { name: '模式识别的基本概念', level: 1 },
        { name: '什么是模式',  level: 1 },
        { name: '什么是识别',  level: 1 },
        { name: '什么是样本',  level: 1 },
        { name: '什么是特征',  level: 1 },
        { name: '什么是类别',  level: 1 },
        { name: '什么是特征提取',  level: 1 },
        { name: '什么是特征选择',  level: 1 },
        { name: '什么是特征向量表示法',  level: 1 },
        { name: '什么是分类决策',  level: 1 },
        { name: '什么是训练',  level: 1 },
        // Level 2: 高级应用节点
        { name: '模板匹配法', level: 2 },
        { name: '统计模式识别', level: 2 },
        { name: '结构模式识别', level: 2 },
        { name: '模糊模式识别', level: 2 },
      ],
      allLinks: []
    };
  },
  mounted() {
    // 组件挂载后初始化图表
  this.initChart();
  },
  created(){
  this.initAllLinks()
  },
  methods: {
    initAllLinks(){
      this.allLinks = this.allNodes.reduce((links, currentNode, index, array) => {
      if (index < array.length - 1) {
        links.push({ source: currentNode.name, target: array[index + 1].name });
      }
      return links;
    }, [])
    },
    initChart() {
      // 初始化 ECharts 实例
      this.chart = echarts.init(this.$refs.chart);
      // 更新图表数据
      this.updateChart();
      // 为图表添加点击事件监听
      this.chart.on('click', this.handleChartClick);
    },
    getNodesAndLinks() {
      // 获取节点和链接的样式和数据
      const highlightedNodes = this.getHighlightedNodes(); // 获取当前需要高亮的节点
      const nodes = this.allNodes.map(node => ({
        ...node,
        itemStyle: {
          // 设置节点的样式
          color: this.getNodeColor(node.level), // 根据节点的级别设置颜色
          opacity: highlightedNodes.includes(node.name) ? 1 : 0.2 // 高亮节点不透明度为1，其余为0.2
        },
        symbolSize: 100, // 节点的大小
        label: {
          show: true // 显示节点标签
        }
      }));

      const links = this.allLinks.map(link => ({
        ...link,
        lineStyle: {
          // 设置链接的样式
          opacity: highlightedNodes.includes(link.source) || highlightedNodes.includes(link.target) ? 0.5 : 0.1 // 高亮的链接不透明度为0.5，其余为0.1
        }
      }));

      return { nodes, links };
    },
    getHighlightedNodes() {
      // 获取当前需要高亮的节点（包括路径上的节点）
      if (!this.highlightedNode) return []; // 如果没有高亮节点，返回空数组

      const highlightedNodes = new Set(); // 使用 Set 存储高亮的节点
      const nodesToCheck = [this.highlightedNode]; // 从当前高亮节点开始检查

      while (nodesToCheck.length) {
        const currentNode = nodesToCheck.pop(); // 取出当前节点
        highlightedNodes.add(currentNode); // 将当前节点标记为高亮

        // 查找并添加当前节点的前置节点
        this.allLinks
          .filter(link => link.target === currentNode)
          .forEach(link => {
            if (!highlightedNodes.has(link.source)) {
              nodesToCheck.push(link.source); // 将前置节点添加到待检查列表中
            }
          });
      }

      return Array.from(highlightedNodes); // 将 Set 转换为数组
    },
    updateChart() {
      // 更新 ECharts 图表
      const { nodes, links } = this.getNodesAndLinks(); // 获取节点和链接的数据

      this.chart.setOption({
        title: {
          text: '模式识别知识图谱', // 图表标题
          left: 'center' // 标题位置
        },
        series: [
          {
            type: 'graph', // 图表类型为图
            layout: 'force', // 使用力导向布局
            symbolSize: 60, // 节点大小
            roam: true, // 是否允许缩放和拖拽
            label: {
              show: true, // 显示标签
              position: 'inside', // 标签位置
              fontSize: 15 // 标签字体大小
            },
            edgeSymbol: ['circle', 'arrow'], // 链接的箭头形状
            edgeSymbolSize: [4, 10], // 链接的箭头大小
            force: {
              repulsion: 1000, // 节点间的排斥力
              edgeLength: [100, 200] // 链接的长度范围
            },
            draggable: true, // 节点是否可拖拽
            data: nodes, // 节点数据
            links: links, // 链接数据
            lineStyle: {
              color: 'source', // 链接的颜色来源
              curveness: 0.3 // 链接的弯曲度
            }
          }
        ]
      });
    },
    getNodeColor(level) {
      // 根据节点的级别返回颜色
      const colors = ['#ff7f50', '#87cdfa', '#da70d6', '#32cd32'];
      return colors[level] || '#cccccc'; // 如果级别超出范围，返回灰色
    },
    handleChartClick(params) {
  if (params.dataType === 'node') {
    const clickedNode = params.data.name;
    const allNodes = this.allNodes.map(node => node.name);
    const links = this.allLinks;

    // 检查前置节点是否全部点亮
    const checkPredecessors = (node) => {
      const predecessors = links
        .filter(link => link.target === node)
        .map(link => link.source);

      const allPredecessorsLit = predecessors.every(predecessor => allNodes.includes(predecessor) && this.getHighlightedNodes().includes(predecessor));

      if (!allPredecessorsLit) {
        alert('需要先点亮前面的节点');
        return false;
      }

      return true;
    };

    // 递归检查前置节点
    let currentNode = clickedNode;
    let canHighlight = true;
    while (canHighlight && currentNode) {
      canHighlight = checkPredecessors(currentNode);
      // 如果当前节点不是根节点，继续检查其前置节点
      if (canHighlight) {
        const parentLink = links.find(link => link.target === currentNode);
        currentNode = parentLink ? parentLink.source : null;
      }
    }

    if (canHighlight) {
      this.highlightedNode = clickedNode;
      this.updateChart(); // 更新图表以反映高亮的节点
    }
  }
}
  }
};
</script>

<style>
#app {
  font-family: Avenir, Helvetica, Arial, sans-serif;
  -webkit-font-smoothing: antialiased;
  -moz-osx-font-smoothing: grayscale;
  text-align: center;
  color: #2c3e50;
  margin-top: 40px;
}
</style>
