# LovezhuoyouAutoCheck
爱桌游（ https://www.lovezhuoyou.com/ ）自动签到脚本，支持腾讯云函数部署

# 使用方法
            
  ***腾讯云函数部署***
          
          1、创建腾讯云函数
          
          2、自定义创建
          
          3、本地上传zip包(https://github.com/nix18/LovezhuoyouAutoCheck/releases/download/V1.0/lovezhuoyou-auto-check.V1.0.zip)
          
          4、index.py中填写cookie_str（通过浏览器登录lovezhuoyou.com, F12 Network标签下获取），
             plus_key（http://www.pushplus.plus/ 的token），部署
               
          5、触发管理->创建定时触发器->自定义触发周期（Cron表达式: 0 0 5 * * * *）->测试完成
  
          
# Licence

[GNU General Public License v3.0](https://raw.githubusercontent.com/nix18/LovezhuoyouAutoCheck/main/LICENSE)


# 作者博客

[Moecola.com](https://moecola.com)
