import java.io.*;
import java.net.*;
import java.util.*;

class Guest extends Thread {
  Socket s;
  Scanner sc;
  OutputStream out;
  Server server;
  String id;

  Guest(Socket s, Server server) {
    try {
      this.server = server;
      this.s = s;
      InputStream in = s.getInputStream();
      sc = new Scanner(in);
      out = s.getOutputStream();
    } catch (Exception e) {
      System.out.println("네트워크 초기화하다가 오류~");
      closeAll();
    }
  }

  void sendMsg(String msg) {
    try {
      out.write((msg + "\n").getBytes());
    } catch (Exception e) {
      System.out.println("보내는중 오류~");
      closeAll();
    }
  }

  public void run() { //클라이언트가 보낸 메시지 읽기. Thread로 가동
    try {
      while (true) {
        String msg = sc.nextLine();
        String[] array = msg.split("/");
        switch (array[0]) {
          case "enter":
            id = array[1];
            server.broadcast(msg);
            server.makeGuestlist();
            break;
          case "msg":
            server.broadcast(msg + "/" + id);
            break;
          case "leave":
            server.deleteGuest(this); // "leave/" 메시지 받을 경우 guestlist에서 해당 guest 삭제
            server.broadcast(msg + id); // "leave/id" 형태로 메시지 broadcast
            server.makeGuestlist(); // 갱신된 guestlist 전송
            break;
        }
      }
    } catch (Exception e) {
      System.out.println("읽어들이는중 오류~");
      closeAll();
    }
  }

  void closeAll() {
    try {
      if (out != null) {
        out.close();
        out = null;
      }
      if (sc != null) {
        sc.close();
        sc = null;
      }
      if (s != null) {
        s.close();
        s = null;
      }
    } catch (Exception e) {
      System.out.println("자원정리중 오류발생~");
    }
  }
}
