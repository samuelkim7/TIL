import java.awt.*;
import java.awt.event.*;
import java.io.*;
import java.net.*;
import java.util.*;

class Client extends Frame implements ActionListener {
  TextArea ta;
  java.awt.List list;
  TextField tf;
  Button b;

  Socket s;
  Scanner sc;
  OutputStream out;

  String id;

  Client(String id) {
    super(id + "님 채팅창");
    this.id = id;
    ta = new TextArea();
    list = new java.awt.List();
    tf = new TextField();
    b = new Button("나가기");

    Panel centerPanel = new Panel();
    Panel southPanel = new Panel();
    centerPanel.setLayout(new BorderLayout());
    southPanel.setLayout(new BorderLayout());
    centerPanel.add(ta);
    centerPanel.add(list, "East");
    southPanel.add(tf);
    southPanel.add(b, "East");

    add(centerPanel);
    add(southPanel, "South");

    tf.addActionListener(this);
    b.addActionListener(this);
  }

  void initNet() {
    try {
      s = new Socket("localhost", 7788);
      InputStream in = s.getInputStream();
      sc = new Scanner(in);
      out = s.getOutputStream();
      sendMsg("enter/" + id);
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

  void readMsg() {
    try {
      while (true) {
        String msg = sc.nextLine();
        String[] array = msg.split("/");
        switch (array[0]) {
          case "enter":
            ta.append("###" + array[1] + "님 입장~\n");
            break;
          case "msg": // [접속자명] + 입력내용 형태로 msg 출력
            ta.append("[" + array[2] + "]" + array[1] + "\n");
            break;
          case "guestlist": // guestlist가 접속자 입장이나 퇴장시 갱신됨
            list.removeAll();
            int size = array.length;
            for (int i = 1; i < size; i++) list.add(array[i]);
            break;
          case "leave": // "leave/id" 메시지 받을 시
            ta.append("###" + array[1] + "님 퇴장~\n");
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

  public void actionPerformed(ActionEvent e) {
    if (e.getSource() == tf) { //textfield에 입력 후 엔터 누를 시 "msg/입력내용" 메시지 전송
      sendMsg("msg/" + tf.getText());
      tf.setText("");
    } else { //"나가기" 버튼 누를 경우 "leave/" 메시지 전송
      sendMsg("leave/");
      setVisible(false);
      dispose();
    }
  }

  public static void main(String args[]) {
    Client client = new Client(args[0]);
    client.initNet();
    client.setBounds(200, 200, 500, 500);
    client.setVisible(true);
    client.readMsg();
  }
}
