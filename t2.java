import java.io.*;
class A{
public static void main(String args[]){
try(
	FileInputStream fis=new FileInputStream("t2.java");
	){
	int size = fis.available();
	byte[] buffer = new byte[size];
	fis.read(buffer);
	System.out.print(new String(buffer));
	}catch(FileNotFoundException e){
	System.out.println("해당파일이 존재하지 않습니다.");
	}catch(IOException e){
	System.out.println("읽거나 쓰다가 오류발생~");
}
}
}