import os
import codecs
import sys
from xlrd import open_workbook

if (len(sys.argv)>=3):
	platform=str(sys.argv[1])
	excel_file=str(sys.argv[2])
else:
	platform=''
	print 'Platform must be added!!'	
if not os.path.exists('out'):
    os.makedirs('out')
else:
	print 'out folder is already exists'

	
wb = open_workbook(excel_file, encoding_override="cp1252")
for s in wb.sheets():
	rows=[]
	for col in range(s.ncols):
		row_value=[]
		for row in range(s.nrows):
			value=(s.cell(row,col).value)
			try : value = str(int(value))
			except : pass
			row_value.append(value)
		rows.append(row_value)		
	
	keys=rows[0]
	
	#counts the languages
	for j in range(1, len(rows)):
		values=rows[j]
		if platform=='AND':
			out_file=codecs.open('out/'+values[0]+'.xml','w', encoding="utf-8")
			out_file.write('<resources>\n')
		elif platform=='IOS':
			out_file=codecs.open('out/'+values[0]+'.strings','w', encoding="utf-8")
			
		for i in range(1, len(keys)):	
			if keys[i]<>'' and not (keys[i].startswith("/*")):
				if platform=='IOS':
					out_file=codecs.open('out/'+values[0]+'.strings','a', encoding="utf-8")
					out_file.write('"'+keys[i]+'" = "'+values[i]+'";\n')	
				elif platform=='AND':
					out_file=codecs.open('out/'+values[0]+'.xml','a', encoding="utf-8")
					out_file.write('<string name="'+keys[i]+'">'+values[i]+'</string>\n')
					
			#else:
				#out_file.write(keys[i]+'\n')
			i=i+1
			
		if platform=='AND':
			out_file.write('</resources>\n')
			
		out_file.close()
		print values[0] +' --> Done'

		
		
