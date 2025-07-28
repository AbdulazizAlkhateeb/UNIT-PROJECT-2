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
