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
		item2.addActionListener(this);
	}
	public void actionPerformed(ActionEvent e){
		if(e.getSource()==item1){
		//파일 열기
		FileDialog fd=new FileDialog(this);
		fd.setVisible(true);
		readFile(fd.getDirectory()+fd.getFile());
		}else{
		//파일 저장
		FileDialog fd=new FileDialog(this, "파일저장", FileDialog.SAVE);
		fd.setVisible(true);
		writeFile(fd.getDirectory()+fd.getFile());
		}
	}

	void writeFile(String fn){
		try(
			FileOutputStream fos = new FileOutputStream(fn);
		){
			byte[] buffer = ta.getText().getBytes();
			fos.write(buffer);
		}catch(IOException e){
			System.out.println("쓰다가 오류발생~");
		}
	}

	void readFile(String fn){
		try(
			FileInputStream fis=new FileInputStream(fn);
		){
			byte[] buffer=new byte[fis.available()];
			fis.read(buffer);
			ta.setText(new String(buffer));
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
