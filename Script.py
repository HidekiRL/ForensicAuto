#Python	 Script Forense

### IMPORTS ###
import subprocess, time, re, io
from subprocess import check_output
from datetime import datetime, date

### FUNCTIONS ###
def cmd(commando):
	proc = subprocess.Popen(commando, shell=True, stdout=subprocess.PIPE)
	for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"): 
		file.write('<p style="font-weight: normal;">'+line+"</p>")

def cmd_table(commando):
	proc = subprocess.Popen(commando, shell=True, stdout=subprocess.PIPE)
	file.write('<table style="width:100%">')
	for line in io.TextIOWrapper(proc.stdout, encoding="utf-8"): 
		file.write('<tr>')
		for word in line.split():
			file.write("<td>"+word+"</td>")
		file.write('<tr>')
	file.write('</table>')
	
### OPEN FILE ###
file = open("Informe.html", "a")
file.flush()

########################################################
file.write('<!DOCTYPE html><html><body>')
file.write('<h2 style = "font-family:Arial;font-style:italic">FORENSIC PRACTICE</h2>')
file.write("<h4>Author : Bani Amundaray Carmona</h4>")
file.write('<hr>')

########################################################

file.write("<h4>Execution Date</h4>")

#Get time
now = datetime.now()
today = date.today()

full_date = today.strftime("%B %d, %Y")
current_time = now.strftime("%H:%M:%S")

file.write("<p>"+full_date +" "+current_time+"</p>")
file.write('<hr>')

file.write("<h4>Machine Name</h4>")

file.flush()
cmd("hostname")

file.write('<hr>')
file.write("<h4>User Accounts Name</h4>")
file.flush()
cmd('wmic useraccount get name | findstr /v "Name" | findstr /rc:"[^ <tab>]"')

file.write('<hr>')
file.write("<h4>Services Running</h4>")
file.flush()
cmd('net start | findstr /v "These Windows services are started:" | findstr /v "The command completed successfully." |  findstr /rc:"[^ <tab>]"')

file.write('<hr>')
file.write("<h4>Process Running</h4>")
file.flush()
cmd('wmic process')

file.write('<hr>')
file.write("<h4>Network Info</h4>")
file.flush()
cmd('ipconfig')

file.write('<hr>')
file.write("<h4>Software Installed<h4>")
file.flush()
cmd('wmic product get name,version | findstr /v "Name" | findstr /v "Version"')

file.write('<hr>')
file.write("<h4>Memory Ram</h4>")
file.flush()
cmd('echo "Y" | DumpIt.exe')
file.write('<p style="font-weight: normal;">File saved successfully</p>')
cmd('dir *.raw* | findstr "raw"')

file.write('<hr>')
file.write("<h4>EVTX Files</h4>")
file.flush()
cmd('gsudo Xcopy /E /I C:\Windows\System32\winevt\Logs Logs')
file.write('<p style="font-weight: normal;">Files saved in folder: Logs</p>')

file.write('<hr>')
file.write("<h4>Pagefile.sys</h4>")
file.flush()
cmd('RawCopy.exe /FileNamePath:C:\pagefile.sys /OutputPath:')
file.write('<p style="font-weight: normal;">File saved successfully</p>')


file.write('<hr>')
file.write("<h4>HKEY_LOCAL_MACHINE</h4>")
file.flush()
cmd('RawCopy.exe /FileNamePath:C:\Windows\System32\config\SAM /OutputPath:')
file.write('<p style="font-weight: normal;">File saved successfully</p>')

file.write("</body></html>")

print("Done!")