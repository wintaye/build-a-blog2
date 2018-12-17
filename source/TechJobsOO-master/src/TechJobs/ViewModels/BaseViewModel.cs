using System;
using System.Collections.Generic;
using System.Linq;
using System.Threading.Tasks;
using TechJobs.Models;

namespace TechJobs.ViewModels
{
    public class BaseViewModel
    {
        public List<JobFieldType> Columns { get; set; }

        public string Title { get; set; } = "";
    }
}
