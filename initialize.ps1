param ( 
  [switch]$Venv, 
  [switch]$Install
)


if ( $Venv ) { python -m venv venv } 
if ( $Install ) { python -m pip install -r .\requirements.txt }
