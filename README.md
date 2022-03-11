
> 利用python整理GitHub的repo和star
python+access_token

python利用GitHub access token 获取仓库信息生成markdown文本

仓库属性字段：
- 标题
- 地址
- 简介
- 标签
- star
- fork
- watch
- main language
- 仓库属性
- 是否组织

配置项：
- 用户名
- access_token
- 排序字段
- 分类字段

markdown
```markdown
# [username](location)
> 用户信息

## 仓库
### 分类1
#### 仓库1`public`
- star：1
- fork：1
- watch：1
> 标签
简介
#### 仓库1
### 分类2


```
