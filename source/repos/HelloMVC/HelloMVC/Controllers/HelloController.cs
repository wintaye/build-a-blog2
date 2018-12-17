using Microsoft.AspNetCore.Mvc;

// For more information on enabling MVC for empty projects, visit https://go.microsoft.com/fwlink/?LinkID=397860

namespace HelloMVC.Controllers
{
    public class HelloController : Controller
    {
        // GET: /<controller>/
        [HttpGet]
        public IActionResult Index(string name = "World")
        {
            string html = "<form method='post'>" +
                "<input type='text' name='name' />" +
                "<select name='language'><option value='english'>English</option>" +
                "<option value='french'>French</option>" +
                "<option value='italian'>Italian</option>" +
                "<option value='amharic'>Amharic</option>" +
                "<option value='spanish'>Spanish</option></select>" +
                "<input type='submit' value='Greet me' />" +
                "</form>";

            return Content(html, "text/html"); 
        }
        // /Hello
        //[Route("/Hello")]
        //[HttpPost]
        //public IActionResult Display (string name)
        //{
            //return Content(string.Format("<h1>Hello, {0}</h1>", name), "text/html");
        //}

        [Route("/Hello")]
        [HttpPost]
        public IActionResult Display(string name, string language = "english")
        {
            //if (language = "english")
            //{
                //return Content(string.Format("<h1>Hello, {0}</h1>", name), "text/html");

            //}
            if (language == "french")
            {
                return Content(string.Format("<h1>Bonjour, {0}</h1>", name), "text/html");

            }
            if (language == "italian")
            {
                return Content(string.Format("<h1>Ciao, {0}</h1>", name), "text/html");

            }
            if (language == "spanish")
            {
                return Content(string.Format("<h1>Hola, {0}</h1>", name), "text/html");

            }
            if (language == "amharic")
            {
                return Content(string.Format("<h1>Selam, {0}</h1>", name), "text/html");

            }
            else
            {
                return Content(string.Format("<h1>Hello, {0}</h1>", name), "text/html");
            }
        }

        // Handle  requests to /Hello/NAME (URL segment as param)
        [Route("/Hello/{name}")]

        public IActionResult Index2(string name)
        {
            return Content(string.Format("<h1>Hello, {0}</h1>", name), "text/html");
        }

        public IActionResult Goodbye()
        {
            return Content("Goodbye");
        }
    }
}
