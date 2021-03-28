package com.fr.chart.web;

import com.fr.base.FRContext;
import com.fr.general.IOUtils;
import com.fr.stable.CodeUtils;
import com.fr.web.core.ActionNoSessionCMD;
import com.fr.web.utils.WebUtils;
import java.io.InputStream;
import javax.servlet.http.HttpServletRequest;
import javax.servlet.http.HttpServletResponse;

// 使用request将文件名传入调用cjkDecode函数解密文件名
// 使用invalidResourcePath函数校验文件是否存在
// 最后使用readResource函数读取文件传输到浏览器上 默认目录为resources
// 其中的privilege.xml里面存储了后台的用户名密码

public class ChartGetFileContentAction extends ActionNoSessionCMD {
    public ChartGetFileContentAction() {
    }

    public void actionCMD(HttpServletRequest var1, HttpServletResponse var2, String var3) throws Exception {
        String var4 = CodeUtils.cjkDecode(WebUtils.getHTTPRequestParameter(var1, "resourcepath"));
        //调用cjkDecode函数解密文件名
        if (!WebUtils.invalidResourcePath(var4)) {//校验文件是否存在
            InputStream var5 = FRContext.getCurrentEnv().readResource(var4);
            //读取文件传输到浏览器上默认目录为resources
            String var6 = IOUtils.inputStream2String(var5);
            var6 = var6.replace('\ufeff', ' ');
            WebUtils.printAsString(var2, var6);
        }
    }

    public String getCMD() {
        return "get_geo_json";
    }
}
