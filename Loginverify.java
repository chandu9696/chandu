import java.io.*;
import javax.servlet.*;
import javax.servlet.http.*;

public class Loginverify extends HttpServlet {
 
    protected void doPost(HttpServletRequest request, HttpServletResponse response)
            throws ServletException, IOException {
        response.setContentType("text/html;charset=UTF-8");
        PrintWriter out = response.getWriter();
        
        String user = request.getParameter("uname");
        String pass = request.getParameter("pname");
        
       if(user.equals("chandu")&&pass.equals("chandu"))
        {
            RequestDispatcher rs = request.getRequestDispatcher("course.jsp");
            rs.forward(request, response);
        }
        else
        {
           out.println("Username or Password incorrect");
           RequestDispatcher rs = request.getRequestDispatcher("index.html");
           rs.include(request, response);
        }
    }  
}