// java -cp ".;postgresql-42.2.18.jar" JavaApplication1

public class Inclusao {

   public static void main(String[] args) {
      String driver = "org.postgresql.Driver";
      String usuario = "ulisses";
      String senha = "123456";
      String url = "jdbc:postgresql://192.168.15.12/bancoteste";
      java.sql.Connection con = null;      
      try {
         Class.forName(driver);
         con = (java.sql.Connection) java.sql.DriverManager.getConnection(url, usuario, senha);
         javax.swing.JOptionPane.showMessageDialog(null, "Conexão realizada!");
      } catch (ClassNotFoundException ex) {
         ex.printStackTrace();
      } catch (java.sql.SQLException e) {
         e.printStackTrace();
      }
		
      java.util.Scanner teclado = new java.util.Scanner(System.in);
      String descricao;
      double preco;
      System.out.print("Informe a descricao: ");
      descricao = teclado.nextLine();
      System.out.print("Informe o preço: ");
      preco = teclado.nextDouble();
		
      String query = "INSERT INTO produtos(codigo,descricao,preco) VALUES((select max(codigo)+1 from produtos),'"+descricao+"',"+preco+")";
				
      try{
         java.sql.Statement st = con.createStatement();		
         st.executeUpdate(query);
         javax.swing.JOptionPane.showMessageDialog(null,"Produto inserido com sucesso!");
         st.close();
         con.close();
      } catch(java.sql.SQLException ex){
         ex.printStackTrace(); 
         javax.swing.JOptionPane.showMessageDialog(null,"Impossível inserir o registro!");
      }
		
   }
    
}