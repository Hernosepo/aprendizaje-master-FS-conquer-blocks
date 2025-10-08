1. Selecciona los elementos div que sean hijos de otro div

   div > div {
   background: red;
   }

2. Selecciona los hijos de los elementos p

   p > \* {
   color: blue;
   }

3. Selecciona los elementos p que sean hijos de article.

   article > p {
   font-size: 50px;
   }

4. Selecciona los p que esten dentro de un article.

   article p {
   color: green;
   }

5. Selecciona los titulos h1 y los h3

   h1, h3 {
   background: grey;
   }

6. Selecciona los ol que esten dentro de body

   body ol {
   font-size: 50px
   }

7. Cualquier elemento que tenga la clase “amarillo"

   .amarillo {
   color: red;
   }

8. Los elementos <ul> que sean hijos de <body>

   body > ul {
   font-size: 50px;
   }

9. Los elementos <a> que sean hijos de <p>

   p > a {
   font-weight: bold;
   }

10. Selecciona el elemento con id “platano"

    #platano {
    color: green;
    }

11. Todos los elementos <div> que sean hermanos de un elemento <h2>

    h2 + div {
    font-weight: bold;
    }

12. Todos los elementos <p> con clase = paisa, descendientes de un elemento <ul>

    ul p.paisa {
    color: red;
    }

13. Selecciona los <h1>, <h2>, <h3> que tengan la clase "headertitle", hijos del header

    header > h1.headertitle,
    header > h2.headertitle,
    header > h3.headertitle
