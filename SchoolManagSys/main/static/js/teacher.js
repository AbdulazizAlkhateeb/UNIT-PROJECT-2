document.addEventListener('DOMContentLoaded', function(){
  var search = document.getElementById('teacherSearch');
  if(search){
    search.addEventListener('input', function(){
      var term = this.value.toLowerCase();
      document.querySelectorAll('.teacher-row').forEach(function(row){
        row.style.display = row.textContent.toLowerCase().includes(term) ? '' : 'none';
      });
    });
  }
});


document.getElementById("classroomSearch").addEventListener("input", function () {
    const value = this.value.toLowerCase();
    document.querySelectorAll(".classroom-row").forEach(row => {
        const text = row.textContent.toLowerCase();
        row.style.display = text.includes(value) ? "" : "none";
    });
});
