# Voice-Control-Mobile-Car

Use CMU Sphinx to voice control raspberry pi to drive the mobile car to the designated position

## 1.摘要

本專題目的是辨識使用者特定語音，並讓自走機器人聽從使用者命令行動。我們以前人的語音辨識經驗與演算法為起點，採用許多語音辨識技巧，匯入語音資料庫進行辨識比對，此實務專題將語音辨識的理論與實作兩者合一，學習到研讀資料、擷取數據、實作程式、分析結果等專題研究的技巧與經驗。

## 2.簡介

科技的日新月異，以機器化代替人力的技術，確實帶給世界上的人更便利且更有效率的生活型態。在語音辨識這方面技術與應用已經趨於成熟的階段，像是運用在手機上，利用人說話輸入來完成各種指令。或是運用在電腦的輸入，可以不用鍵盤，透過麥克風，說的話即可立即顯示成文字。由於好奇心理，開啟了我們對於語音辨識領域的初步了解。
語音的技術有很多種，我們主要做語音辨認(speech recognition)，用CMU Sphinx系統為基礎，讓機器聽懂人說的話，即為自動語音辨認。我們專題的主要目的，在於學習現有的語音辨識理論與技巧。經由實作經驗，結合所學到的知 識，一步一步學以致用。
我們期望製作出的語音控制車可以成為讓我們與智慧家庭領域接軌的橋樑，與快速發展中的智能家庭概念接軌。智慧家庭是由家中裝置互聯產生的生態系統，其核心概念是，讓家中裝置能更好的解決用戶在居家環境中常發生的問題，同時。更確切的說，智慧家庭意在讓用戶的生活變得更加安全、便利、節能、甚至降低支出、與增加娛樂價值。因此，我們期望製作出的智能自走車可以達成便利性的目的，便利化使用者的生活。

## 3.專題進行方式

研究步驟為:CMU Sphinx 安裝至樹梅派上進行語音辨識並控制我們所撰寫之 python 程式，輸出訊號至自走車馬達驅動板 L298N 上，使 DC 馬達驅動，控制自走車完成目的。
A.將語音辨識的理論與實作兩者合一，利用研讀資料、擷取數據、實作程式等方式將樹梅派與自走車整合。需熟用 Linux 指令將 CMU Sphinx 系統安裝至樹梅派上，並自撰程式碼將樹梅派與 DC 直流引擎連動，過程均組員二人合作完成。
![image](https://github.com/ChuHanLin0923/ChuHanLin/blob/main/1.png)

B.Sphinx 的實現方法採用隱藏式馬可夫模型 (HMM)架構，建基於馬可夫鏈模型，其中規定指定狀態的機率取決於現行狀態而非其先前狀態。雖然馬可夫鏈模型對於可觀察的事件，例如文字輸入很有用，但隱藏式馬可夫模型可讓我們將隱藏事件，例如:詞類標註納入機率模型中。它們在語音辨識中用作序列模型，將標籤分配給序列中的每個單元，即字詞、音節、句子等。這些標籤會在其與所提供的輸入之間建立對映，以便它判斷最適當的標籤序列。

C.開源軟件 Sphinx 辨識語音良率不佳
解決途徑:利用 CMU 發行的線上開源程式 LMtool[註 1]自行建立一個語料庫，縮小語音辨識範圍。
![image](https://github.com/ChuHanLin0923/ChuHanLin/blob/main/4..png)

D. 樹梅派連接 L298n 驅動板後，可見左下圖為自走車系統的電路圖。Two_motor.py 將樹梅派指定腳位之電壓傳送到 L298n，其中 IN1、IN2 控制其中 1 顆 DC 馬達，IN3、IN4 控制另外一顆，晶片輸入與馬達狀態關係可見右下的圖表。
![image](https://github.com/ChuHanLin0923/ChuHanLin/blob/main/2.jpg)
![image](https://github.com/ChuHanLin0923/ChuHanLin/blob/main/3..png)
## 4.主要成果與評估

我們專題的主要目的，在於學習現有的語音辨識理論與技巧，用 CMU Sphinx 系統為基礎，讓機器聽懂人說的話，完成自動語音辨認。經由實作經驗，結合所學到的知識，一步步學以致用。
我們期望製作出的語音控制車可以應用在:

A. 智慧家庭領域
智慧家庭概念的興起改善人們的生活，自走車可以完成我們交代的大小瑣事，例如:發懶時想拿取一包零食、搬運重物、包裹等

B. 醫療照護領域
對於雙腿不方便的使用者，自走車可以成為好的幫手，搖身一變成:送餐車、移動輪椅車等

(1) 將所學知識應用在樹莓派上，製作一個聲控自走車與智慧家庭概念接軌，
提升對於工程應用的除錯技術、熟練 Linux 系統的相關指令、對開源語音辨識系統的認識、將所學知識發揮在製作專題過程中，並對工程技術與通訊系統概念更為熟悉。

(2) 具體之成果:喊出不同指定單詞，自走車能夠行動至不同指定地點並停下。

(3) 與預期成果之差異:由於運送物品該自走車無法負擔重量，且路徑之控制無法做到非常精確，我們將其簡化為喊出不同指定單詞，自走車能夠行動至不同指定地點。

(4) 未來可能之擴展方向:若未來車子在負重上能夠得到改善，且語音辨識能夠精確辨識更多單詞及車子能夠行走較複雜之指令，便可以執行複雜指令，並將其實際用於智慧家庭生活及醫療照護中，我們預期能夠將其運用於在室內區域運送物品，並利用此聲控自走車使生活更加便利。

## 5.結語與展望

在這次專題中，我們提升對於工程應用的除錯技術、熟練Linux系統的相關指令、對開源語音辨識系統的了解與應用、將所學知識發揮在製作專題過程中，並對工程技術與通訊系統概念更為熟悉。
未來希望仍有機會能夠參與類似的專題或研究，並利用此次經驗使得操作更加熟練，以完成不同應用之開發，並將其利用於現實生活中。
在此次專題中我們意識到有些東西的不足，例如自走車的穩定性及乘載力的不足，以及希望能更換供電及語音傳輸的方式，使得自走車能夠真正的無線控制，如果以後還有機會希望能夠改進這些缺點。

## 6.Demo 影片
https://www.youtube.com/watch?v=Unp9Dzj8iNI
