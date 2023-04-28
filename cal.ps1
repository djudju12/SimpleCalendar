
function cal {
   param (
      [string] $date
   )
   

   if(-not $date){
      py C:\Users\jonathan.santos\Desktop\unisc\SimpleCalendar\SimpleCalendar.py
   } else {
      &py C:\Users\jonathan.santos\Desktop\unisc\SimpleCalendar\SimpleCalendar.py $date
   }

}
