import java.io.*;
import java.net.*;
import java.util.*;

class Server {
  ServerSocket ss;
  List<Guest> list;

  void initNet() { //네트워크 초기화
    try {
      list = new ArrayList<Guest>();
      ss = new ServerSocket(7788);
      while (true) {
        Socket s = ss.accept();
        Guest guest = new Guest(s, this); //Guest 객체 생성 및 Socket 전달
        guest.start(); //guest 읽기 Thread 시작
        addGuest(guest);
      }
    } catch (Exception e) {
      System.out.println(e);
      System.out.println("네트워크 초기화하다가 오류~");
      closeAll();
    }
  }

  void addGuest(Guest guest) { //guest 입장시 list에 추가
    list.add(guest);
    System.out.println("접속자수:" + list.size());
  }

  void deleteGuest(Guest guest) {
    list.remove(guest); //guest 퇴장시 list에서 삭제
    System.out.println("접속자수:" + list.size());
  }

  void broadcast(String msg) { //guest로부터 msg를 받으면 모든 client에게 broadcasting
    for (Guest guest : list) guest.sendMsg(msg);
  }

  void makeGuestlist() { //guest list를 String으로 변환하여 broadcasting
    StringBuffer buffer = new StringBuffer("guestlist/");
    for (Guest guest : list) {
      buffer.append(guest.id);
      buffer.append("/");
    }
    broadcast(buffer.toString());
  }

  void closeAll() { //자원 정리
    try {
      if (ss != null) {
        ss.close();
        ss = null;
      }
    } catch (Exception e) {
      System.out.println("자원정리중 오류발생~");
    }
  }

  public static void main(String args[]) {
    Server server = new Server();
    server.initNet();
  }
}
