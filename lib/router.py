import lib.model as model

class Router:
    @staticmethod
    def run(app):
        
        @app.route('/')
        def root():
            return model.getRootData()

        @app.route('/daftar-komik')
        def daftar_komik():
            return model.getDaftarKomik()
			
        @app.route('/komikgenre')
        def komikgenre():
            return model.getKomikGenre()
			
        @app.route('/project-list')
        def project_list():
            return model.getProjectList()
        
        @app.route('/komik-tamat')
        def komik_tamat():
            return model.getKomikTamat()
        
        @app.route('/jadwal-update')
        def jadwal_update():
            return model.getJadwalUpdate()

        @app.route('/komik')
        def komik():
            return model.getDataKomik()
        
        @app.route('/chapter')
        def chapter():
            return model.getChapterComic()
			
        @app.route('/genre')
        def genre():
            return model.getGenre()
			
        @app.route('/search')
        def search():
            return model.getSpecificComic()
			
		
            

