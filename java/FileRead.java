//Modal 창에서 파일을 선택하고, 선택된 파일의 내용을 TextArea에 출력
//파일 선택과 파일명을 가져오기 위해 FileDialog 사용
//파일 내용을 읽어오는 readFile이라는 Method 정의

import java.awt.*;
import java.awt.event.*;
import java.io.*;
class A extends Frame implements ActionListener{
MenuItem item1,item2;
Menu m;
MenuBar mb;
TextArea ta;
A(){
item1=new MenuItem("열기");
item2=new MenuItem("저장");
m=new Menu("파일");
m.add(item1);
m.add(item2);
mb=new MenuBar();
mb.add(m);
setMenuBar(mb);
ta=new TextArea();
add(ta);

item1.addActionListener(this);
}
public void actionPerformed(ActionEvent e){
FileDialog fd=new FileDialog(this);
fd.setVisible(true);
readFile(fd.getDirectory()+fd.getFile());
}

void readFile(String fn){
try(
FileInputStream fis=new FileInputStream(fn);
){
int size = fis.available();
byte[] buffer = new byte[size];
fis.read(buffer);
{
ta.append(new String(buffer));
}
}catch(FileNotFoundException e1){
System.out.println("해당파일 없어요~");
}catch(IOException e2){
System.out.println("읽다가 오류발생~");
}
}
}
class B{
public static void main(String args[]){
A f=new A();
f.setBounds(100,100,500,500);
f.setVisible(true);
}
}