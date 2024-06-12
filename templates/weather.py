weather = '''<?xml version="1.0" encoding="UTF-8"?>
<ui version="4.0">
 <class>MainWindow</class>
 <widget class="QMainWindow" name="MainWindow">
  <property name="enabled">
   <bool>true</bool>
  </property>
  <property name="geometry">
   <rect>
    <x>0</x>
    <y>0</y>
    <width>1030</width>
    <height>750</height>
   </rect>
  </property>
  <property name="minimumSize">
   <size>
    <width>1030</width>
    <height>750</height>
   </size>
  </property>
  <property name="maximumSize">
   <size>
    <width>16777215</width>
    <height>16777215</height>
   </size>
  </property>
  <property name="font">
   <font>
    <family>DejaVu Sans Mono</family>
    <pointsize>10</pointsize>
    <bold>true</bold>
   </font>
  </property>
  <property name="windowTitle">
   <string>SimpleWeather</string>
  </property>
  <widget class="QWidget" name="centralwidget">
   <layout class="QGridLayout" name="gridLayout">
    <item row="0" column="0">
     <widget class="QWidget" name="widget" native="true">
      <layout class="QGridLayout" name="gridLayout_2">
       <item row="0" column="1">
        <widget class="QLineEdit" name="place"/>
       </item>
       <item row="0" column="2">
        <layout class="QHBoxLayout" name="horizontalLayout">
         <item>
          <widget class="QPushButton" name="btn_change_place">
           <property name="text">
            <string>Изменить место</string>
           </property>
          </widget>
         </item>
        </layout>
       </item>
       <item row="0" column="0">
        <widget class="QPushButton" name="btn_update">
         <property name="text">
          <string>Обновить</string>
         </property>
        </widget>
       </item>
      </layout>
     </widget>
    </item>
    <item row="1" column="0">
     <widget class="QTextBrowser" name="Weather">
      <property name="html">
       <string>&lt;!DOCTYPE HTML PUBLIC &quot;-//W3C//DTD HTML 4.0//EN&quot; &quot;http://www.w3.org/TR/REC-html40/strict.dtd&quot;&gt;
&lt;html&gt;&lt;head&gt;&lt;meta name=&quot;qrichtext&quot; content=&quot;1&quot; /&gt;&lt;meta charset=&quot;utf-8&quot; /&gt;&lt;style type=&quot;text/css&quot;&gt;
p, li { white-space: pre-wrap; }
hr { height: 1px; border-width: 0; }
li.unchecked::marker { content: &quot;\2610&quot;; }
li.checked::marker { content: &quot;\2612&quot;; }
&lt;/style&gt;&lt;/head&gt;&lt;body style=&quot; font-family:'DejaVu Sans Mono'; font-size:10pt; font-weight:700; font-style:normal;&quot;&gt;
&lt;p style=&quot;-qt-paragraph-type:empty; margin-top:0px; margin-bottom:0px; margin-left:0px; margin-right:0px; -qt-block-indent:0; text-indent:0px;&quot;&gt;&lt;br /&gt;&lt;/p&gt;&lt;/body&gt;&lt;/html&gt;</string>
      </property>
     </widget>
    </item>
   </layout>
  </widget>
  <widget class="QStatusBar" name="statusbar"/>
 </widget>
 <resources/>
 <connections/>
</ui>'''