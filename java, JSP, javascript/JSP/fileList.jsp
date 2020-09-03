<!-- 해당 프로젝트 내의 파일명을 출력하고, 파일명 클릭시 해당 파일로 링크 -->

<%@ page import = "java.io.File" %>
<%@ page language="java" contentType="text/html; charset=UTF-8"
    pageEncoding="UTF-8"%>
<!DOCTYPE html PUBLIC "-//W3C//DTD HTML 4.01 Transitional//EN" "http://www.w3.org/TR/html4/loose.dtd">
<html>
<head>
<meta http-equiv="Content-Type" content="text/html; charset=UTF-8">
<title>Insert title here</title>
</head>
<body>
<%
File f=new File(application.getRealPath("/"));     // 해당 프로젝트의 경로 가져옴
for(File ff: f.listFiles()){
	if(ff.isFile()){
		out.print("<a href="+ff.getName()+">");        // 링크 생성
		out.print(ff.getName());
		out.print("</a>");
		out.print("<br>");
	}
}
%>
</body>
</html>
