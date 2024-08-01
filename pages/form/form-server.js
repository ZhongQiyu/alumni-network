// pages/form/form-server.js

const express = require('express');
const app = express();
app.use(express.json());

let formSubmissions = [];  // 模拟数据库存储表单提交记录

// 提交表单
app.post('/submit-form', (req, res) => {
    const { formId, memberId, completed } = req.body;

    // 更新或添加提交记录
    const submission = formSubmissions.find(s => s.formId === formId && s.memberId === memberId);
    if (submission) {
        submission.completed = completed;
    } else {
        formSubmissions.push({ formId, memberId, completed });
    }

    res.status(200).send('Form submission recorded');
});

// 获取总进度
app.get('/progress', (req, res) => {
    const totalForms = 10;  // 假设每个会员有 10 个表单要填写
    const completedForms = formSubmissions.filter(s => s.completed).length;
    const totalProgress = (completedForms / (totalForms * formSubmissions.length)) * 100;

    res.status(200).json({ totalProgress: totalProgress.toFixed(2) + '%' });
});

app.listen(3000, () => console.log('Server running on port 3000'));
