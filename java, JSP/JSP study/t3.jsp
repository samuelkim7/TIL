<!-- 각각의 색 클릭시 해당 색을 parameter로 전달 -->

<%@ page language="java" contentType="text/html; charset=UTF-8"
pageEncoding="UTF-8"%>
<!DOCTYPE html>
<html>
<head>
<meta charset="UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
String[] array={"red","green","blue"};
for(String s: array){
	out.write("<a href=t4.jsp?color="+s+">");
	out.write(s+"</a></br>");
}
%>
</body>
</html>
