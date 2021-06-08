# JAPT-DLUT-

功能： 自动完成JAPT作业操作并截图

-------------------------------------------

prerequisite：
  环境：Mac （因为没找Windows64位的chromedriver）
       python 下载地址http://npm.taobao.org/mirrors/python/
       
    
  版本：找你Chrome对应版本的driver（没对应选最近的）。 下载地址：http://npm.taobao.org/mirrors/chromedriver/
                                  注：查询你的chrome版本。（百度搜索UA，点开分析工具之类；或者从settings的About Chrome里看。如：Version 91.0.4472.77）
                                  
  terminal那里 pip install selenium
  
  我用的pyCharm.可能需要Preferences里调一下Project Structure
  

run：
    前几行，name改成自己学号，password登录密码，screenshot_path你想要存储截屏的目录。browser = webdriver.Chrome()第一个参数改成你下载的chromedriver的地址。
    然后运行，看着就行了，不用动他。
    
    
------------------------------------------

写得仓促，若感觉截屏没截到你想的部分上，需回头自己再截一下。

若将来那个企业更改代码导致运行失败，我也不想再改代码了。

报告自己写吧。

-------------------------------------

免责声明：
    本代码之目的在于帮助同学们学习，节约时间。请同学们不要用它来代替自己完成作业。
    若学生用此代码而非自己操作，本人概不负责。
    
