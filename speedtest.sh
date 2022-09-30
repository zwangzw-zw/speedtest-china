SERVERS="25858 43752 35722 24447 36646 41852"

for i in $SERVERS;
        do 
                
                /opt/speedtest -p no -s $i  
                
done



#/opt/speedtest -s 25858	#China Mobile Group Beijing Co.Ltd	speedtest.bmcc.com.cn.prod.hosts.ooklaserver.net
#/opt/speedtest -s 43752	#BJ Unicom	beijing.unicomtest.com
#/opt/speedtest -s 35722 #TJ Telecom tjrate.tjtele.com 

#/opt/speedtest -s 24447	#China Unicom 5G	5g.shunicomtest.com.prod.hosts.ooklaserver.net
#/opt/speedtest -s 3633	#China Telecom	speedtest1.online.sh.cn
#/opt/speedtest -s 25637	#Chinamobile-5G	speedtest4.sh.chinamobile.com.prod.hosts.ooklaserver.net

#/opt/speedtest -s 36646	#China Unicom HeNan 5G	5gtest.shangdu.com
#/opt/speedtest -s 41852	#河南电信5G	telecomspeed.top.prod.hosts.ooklaserver.net
#/opt/speedtest -s 41910	#China Mobile Henan 5G	speedtest.eastcom.site.prod.hosts.ooklaserver.net
#/opt/speedtest -s 44176	#河南移动5G	5ghenan.ha.chinamobile.com.prod.hosts.ooklaserver.net

#/opt/speedtest -s 27154	#ChinaUnicom-5G	speedtest3.online.tj.cn.prod.hosts.ooklaserver.net
#/opt/speedtest -s 35722	#China Telecom TianJin	tjrate.tjtele.com.prod.hosts.ooklaserver.net
#/opt/speedtest -s 34115	#China Telecom TianJin-5G	sy.tjtele.com.prod.hosts.ooklaserver.net
