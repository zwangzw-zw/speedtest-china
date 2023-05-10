curl --user-agent "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/112.0" -s "https://beta.speedtest.net/api/js/servers?engine=js&search=china&limit=200" | jq -r '.[] | select(.country == "China") | "\(.name) \(.sponsor),\(.id)"' | awk -F ',' '{printf "\033[1;31m%s\033[0m\n", $1; system("/opt/speedtest -s" $2)}'     

#SERVERS="25858 25637 43752 35722 24447 36646 41852"

#SERVERS="25858" # 29105 44176 26940 16145 35722"

#for i in $SERVERS;
#        do 
#                
#                /opt/speedtest -p no -s $i  
#                
#done


sudo nexttrace 36.112.185.161
sudo nexttrace 223.72.127.191

#/opt/speedtest -s 25858	#China Mobile Group Beijing Co.Ltd	speedtest.bmcc.com.cn.prod.hosts.ooklaserver.net
#/opt/speedtest -s 43752	#BJ Unicom	beijing.unicomtest.com
#/opt/speedtest -s 35722        #TJ Telecom tjrate.tjtele.com 

#/opt/speedtest -s 24447	#China Unicom 5G	5g.shunicomtest.com.prod.hosts.ooklaserver.net
#/opt/speedtest -s 3633	        #China Telecom	speedtest1.online.sh.cn
#/opt/speedtest -s 25637	#Chinamobile-5G	speedtest4.sh.chinamobile.com.prod.hosts.ooklaserver.net

#/opt/speedtest -s 36646	#China Unicom HeNan 5G	5gtest.shangdu.com
#/opt/speedtest -s 41852	#河南电信5G	telecomspeed.top.prod.hosts.ooklaserver.net
#/opt/speedtest -s 41910	#China Mobile Henan 5G	speedtest.eastcom.site.prod.hosts.ooklaserver.net
#/opt/speedtest -s 44176	#河南移动5G	5ghenan.ha.chinamobile.com.prod.hosts.ooklaserver.net

#/opt/speedtest -s 27154	#ChinaUnicom-5G	speedtest3.online.tj.cn.prod.hosts.ooklaserver.net
#/opt/speedtest -s 35722	#China Telecom TianJin	tjrate.tjtele.com.prod.hosts.ooklaserver.net
#/opt/speedtest -s 34115	#China Telecom TianJin-5G	sy.tjtele.com.prod.hosts.ooklaserver.net
