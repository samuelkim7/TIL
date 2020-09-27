function uploadPreview(){
			console.log("updatePreview invoked");
			const preview = document.getElementById("preview");
			const filelist = inputFiles.files;
			if(filelist.length == 0){
				var text = "선택된 파일이 없습니다.";
				preview.innerHTML = text;
			} else {
				var text = "<ul>";
				for(const file of filelist) {
					console.log(file);
					var size = Math.round( parseFloat(file.size) / 1000 );
					text += "<li>" + file.name + " (" + size + " kb)" + "</li>";
				}
				text += "</ul>";
				preview.innerHTML = text;
			}
		}