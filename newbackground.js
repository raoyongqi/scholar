const allowedUrls = [
    "coursesteach.com",
    "rustup.rs",
    "cal-tek.eu",
    "serpapi.com",
    "shizuku.rikka.app",
    "bookdown.org",
    "tspace.library.utoronto.ca",
    "frida.re",
    "changfengbox.top",
    "hm.baidu.com",
    "jstatsoft.org",
    "*.aliyuncs.com",
    "osf.io",
    "*.nih.gov",
    "dlib.hust.edu.vn",
    "nber.org",
    "jstnar.iut.ac.ir",
    "aloki.hu",
    "citeseerx.ist.psu.edu",
    "boa.unimib.it",
    "zlxb.zafu.edu.cn",
    "playwright.dev",
    "iforest.sisef.org",
    "iris.unitn.it",
    "archium.ateneo.edu",
    "onlinelibrary.wiley.com",
    "dsr.inpe.br",
    "thuvienso.hoasen.edu.vn",
    "ebooks.iospress.nl",
    "search.ebscohost.com",
    "git-scm.com",
    "ambridge.org",
    "*.acm.org",
    "*.berkeley.edu",
    "geopandas.org",
    "orbilu.uni.lu",
    "*.amap.com",
    "logic.pdmi.ras.ru",
    "zenodo.org",
    "eric.ed.gov",
    "*.siam.org",
    "essay.utwente.nl",
    "lit2talks.com",
    "*.tidymodels.org",
    "pure.iiasa.ac.at",
    "*.jinshujucdn.com",
    "ssl.ptlogin2.graph.qq.com",
    "academicradiology.org",
    "iaeng.org",
    "cse.fau.edu",
    "*.cloudfront.net",
    "research-repository.griffith.edu.au",
    "agupubs.onlinelibrary.wiley.com",
    "pubs.rsna.org",
    "*.github.com",
    "researchportal.murdoch.edu.au",
    "bjo.bmj.com",
    "publish.mersin.edu.tr",
    "*.oaistatic.com",
    "wires.onlinelibrary.wiley.com",
    "*.alipayobjects.com",
    "books.google.com",
    "*.biologists.com",
    "*.scienceconnect.io",
    "*.azure.com",
    "jsj.top",
    "flore.unifi.it",
    "ijprems.com",
    "indianecologicalsociety.com",
    "eprints.qut.edu.au",
    "passmark.com",
    "img-prod-cms-rt-microsoft-com.akamaized.net",
    "seas.upenn.edu",
    "scrapy.org",
    "sentic.net",
    "*.alipay.com",
    "kimi.com",
    "researchgate.net",
    "strongvpn.com",
    "google.com",
    "*.dkut.ac.ke",
    "aclanthology.org",
    "ira.lib.polyu.edu.hk",
    "*.newrelic.com",
    "academicjournals.org",
    "cdnsciencepub.com",
    "github.com",
    "springer.com",
    "deeplearning.ir",
    "*.usgs.gov",
    "spiedigitallibrary.org",
    "content.iospress.com",
    "*.aegis.qq.com",
    "sp0.baidu.com",
    "repository.kaust.edu.sa",
    "etd.ohiolink.edu",
    "*.nvidia.com",
    "publichealth.jmir.org",
    "lib.iitta.gov.ua",
    "g.3gl.net",
    "besjournals.onlinelibrary.wiley.com",
    "*.nature.com",
    "aiej.org",
    "papers.ssrn.com",
    "*.hanspub.org",
    "codelibrary.info",
    "*.jinshujufiles.com",
    "*.jsdelivr.net",
    "ajce.aut.ac.ir",
    "alyssax.com",
    "connormwood.com",
    "essopenarchive.org",
    "wins.or.kr",
    "alipay.com",
    "docs.geetest.com",
    "philsci-archive.pitt.edu",
    "repository.fit.edu",
    "*.gstatic.com",
    "redux.js.org",
    "pubs.rsc.org",
    "*.126.net",
    "academia.edu",
    "luminati.io",
    "bg.copernicus.org",
    "ere.ac.cn",
    "embopress.org",
    "calhoun.nps.edu",
    "dbpia.co.kr",
    "mae.ucf.edu",
    "microsoft.com",
    "authorea.com",
    "yadda.icm.edu.pl",
    "portlandpress.com",
    "service.seamlessaccess.org",
    "digital.wpi.edu",
    ",*.cnzz.com",
    "*.captcha.qq.com",
    "repositories.lib.utexas.edu",
    "pages.charlotte.edu",
    "repositori.upf.edu",
    "acikerisim.fsm.edu.tr",
    "scholar.archive.org",
    "gitlab.com",
    "ietresearch.onlinelibrary.wiley.com",
    "vldb.org",
    "pmc.ncbi.nlm.nih.gov",
    "nowpublishers.com",
    "journals.asm.org",
    "*.alibabachengdun.com",
    "wiley.com",
    "cdn.techscience.cn",
    "*.qt.io",
    "docs.huihoo.com",
    "opus.bibliothek.uni-augsburg.de",
    "*.journal-grail.science",
    "matplotlib.org",
    "googletagmanager.com",
    "tandfonline.com",
    "unitec.ac.nz",
    "dspace.rsu.lv",
    "ageconsearch.umn.edu",
    "*.psu.edu",
    "ajol.info",
    "cmap.polytechnique.fr",
    "f-droid.org",
    "redux-toolkit.js.org",
    "*.microsoftonline.com",
    "preprints.org",
    "*.googlesyndication.com",
    "react-redux.js.org",
    "datascienceassn.org",
    "cs.ucy.ac.cy",
    "numfocus.org",
    "rmets.onlinelibrary.wiley.com",
    "bit.ly",
    "*.githubusercontent.com",
    "ncbi.nlm.nih.gov",
    "lgincdnvzeuno.azureedge.net",
    "acsess.onlinelibrary.wiley.com",
    "epub.uni-regensburg.de",
    "brgm.hal.science",
    "josis.org",
    "kaggle.com",
    "docs.neu.edu.tr",
    "ant.design",
    "gmd.copernicus.org",
    "gram.web.uah.es",
    "learningsys.org",
    "*.apta.gov.cn",
    "*.deno.dev",
    "run.unl.pt",
    "idl.iscram.org",
    "elsevier.com",
    "ifej.sanru.ac.ir",
    "projectstorm.cloud",
    "figshare.com",
    "zwang4.github.io",
    "platform-api.sharethis.com",
    "scitepress.org",
    "www5.informatik.uni-erlangen.de",
    "heinonline.org",
    "learning1to1.net",
    "journals.plos.org",
    "wps.com",
    "engrxiv.org",
    "direct.mit.edu",
    "scholarworks.smith.edu",
    "dline.info",
    "bmjopen.bmj.com",
    "ui.adsabs.harvard.edu",
    "xyflow.com",
    "*.netzel.pl",
    "*.tensorflow.org",
    "fonts.gstatic.com",
    "researchsquare.com",
    "courses.cs.duke.edu",
    "geoviews.org",
    "tianditu.gov.cn",
    "bme.ufl.edu",
    "iris.unipa.it",
    "sci-hub.gg",
    "ri.conicet.gov.ar",
    "digital.csic.es",
    "sciendo.com",
    "alvinang.sg",
    "eprints.umsida.ac.id",
    "ojs.lib.unideb.hu",
    "drpress.org",
    "spatial.usc.edu",
    "duo.uio.no",
    "structuraltopicmodel.com",
    "*.arxiv.org",
    "ingentaconnect.com",
    "holoviews.org",
    "acnsci.org",
    "epub.ub.uni-greifswald.de",
    "open.bu.edu",
    "pubs.aip.org",
    "*.google.de",
    "*.google.com",
    "docs-neteasecloudmusicapi.vercel.app",
    "icir.org",
    "jamanetwork.com",
    "*.rsc.org",
    "captcha.gtimg.com",
    "degruyter.com",
    "incaindia.org",
    "keras.io",
    "journal.lu.lv",
    "ajnr.org",
    "ideas.repec.org",
    "thilowellmann.de",
    "cs.cmu.edu",
    "revues.imist.ma",
    "ij-aquaticbiology.com",
    "bam.nr-data.net",
    "elibrary.ru",
    "ecmlpkdd2017.ijs.si",
    "*.cloudflare.com",
    "klab.tch.harvard.edu",
    "journals.ametsoc.org",
    "sure.sunderland.ac.uk",
    "bsssjournals.onlinelibrary.wiley.com",
    "taylorfrancis.com",
    "intereuroconf.com",
    "jmlr.org",
    "powertechjournal.com",
    "digitalcommons.memphis.edu",
    "flowchart.js.org",
    "ideals.illinois.edu",
    "arlis.org",
    "royalsocietypublishing.org",
    "mental.jmir.org",
    "seer.ufu.br",
    "jscholarship.library.jhu.edu",
    "dataorigami.net",
    "marginaleffects.com",
    "*.microsoft.com",
    "ffmpeg.org",
    "tauri.app",
    "*.strongvpn.com",
    "journals.sagepub.com",
    "*.unl.edu",
    "k0d.cc",
    "www.52pojie.cn",
    "ggepi.lukewjohnston.com",
    "egusphere.copernicus.org",
    "search.ieice.org",
    "gee-community-catalog.org",
    "iwaponline.com",
    "arodes.hes-so.ch",
    "helda.helsinki.fi",
    "admis.tongji.edu.cn",
    "scitools.org.uk",
    "ece.neu.edu",
    "dam-oclc.bac-lac.gc.ca",
    "*.osgeo.org",
    "*.music.126.net",
    "ddkang.github.io",
    "drive.google.com",
    "*.informs.org",
    "*.codabench.org",
    "esajournals.onlinelibrary.wiley.com",
    "fondazionemcr.it",
    "*.openai.com",
    "*.simpleanalyticscdn.com",
    "arcgis.com",
    "*.oaiusercontent.com",
    "gdal.org",
    "climatechange.ai",
    "escholarship.org",
    "*.alicdn.com",
    "pytorch.org",
    "era.library.ualberta.ca",
    "dada.cs.washington.edu",
    "*.s3.amazonaws.com",
    "openaging.com",
    "dspace.mit.edu",
    "*.163.com",
    "cabidigitallibrary.org",
    "oneecosystem.pensoft.net",
    "*.hubspot.com",
    "ascelibrary.org",
    "elib.psu.by",
    "bdtd.ibict.br",
    "openjournals.uwaterloo.ca",
    "ejournal.svgacademy.org",
    "sciltp.com",
    "ecoevorxiv.org",
    "*.gongkaoshequ.com",
    "mediatum.ub.tum.de",
    "opg.optica.org",
    "webthesis.biblio.polito.it",
    "durham-repository.worktribe.com",
    "badge.dimensions.ai",
    "editor.md.ipandao.com",
    "prodregistryv2.org",
    "ejournal.undip.ac.id",
    "esann.org",
    "*.office.net",
    "wandoujia.com",
    "bigr.io",
    "*.qqmail.com",
    "keevin60907.github.io",
    "mermaid.js.org",
    "*.epfl.ch",
    "soil.copernicus.org",
    "personales.upv.es",
    "*.silverchair.com",
    "theses.hal.science",
    "lmb.informatik.uni-freiburg.de",
    "vite.dev",
    "science.org",
    "*.ptlogin2.qq.com",
    "sci2s.ugr.es",
    "*.nasa.gov",
    "*.ucdl.pp.uc.cn",
    "*.aligames.com",
    "*.mdpi-res.com",
    "*.rust-lang.org",
    "scholarworks.calstate.edu",
    "*.cdn-go.cn",
    "httpbin.org",
    "puiij.com",
    "mocom.xmu.edu.cn",
    "par.nsf.gov",
    "econstor.eu",
    "research.tue.nl",
    "air.ashesi.edu.gh",
    "gbpihed.gov.in",
    "mhealth.jmir.org",
    "pubs.acs.org",
    "scielo.org.mx",
    "*.googlesource.com",
    "uwe-repository.worktribe.com",
    "*.kaggle.com",
    "res.wx.qq.com",
    "pgmpy.org",
    "figshare.utas.edu.au",
    "journals.physiology.org",
    "ocgy.ubc.ca",
    "*.typekit.net",
    "michaelfullan.ca",
    "jstage.jst.go.jp",
    "api.altmetric.com",
    "*.wpscdn.com",
    "*.cloudflareinsights.com",
    "*.theoj.org",
    "*.adobedtm.com",
    "scholar.smu.edu",
    "softcomputing.net",
    "sciencedirect.com",
    "featureassets.org",
    "ecology.ghislainv.fr",
    "apktool.org",
    "biodiversity-science.net",
    "digital.lib.washington.edu",
    "academic-pub.org",
    "aka.ms",
    "*.npmjs.com",
    "cummings-lab.org",
    "gitlab.jsc.fz-juelich.de",
    "aimspress.com",
    "scielo.br",
    "cv-foundation.org",
    "ieeeprojects.eminents.in",
    "bibliotekanauki.pl",
    "*.qutebrowser.org",
    "agritrop.cirad.fr",
    "*.kaggle.io",
    "accounts.google.de",
    "hackveda.in",
    "orbi.uliege.be",
    "epstem.net",
    "projecteuclid.org",
    "*.sciencedirect.com",
    "shubhanshu.com",
    "usenix.org",
    "cbml.science",
    "*.cgiar.org",
    "researchportal.hw.ac.uk",
    "ntnuopen.ntnu.no",
    "dl.acm.org",
    "github.githubassets.com",
    "wechat-article-exporter.deno.dev",
    "kalaharijournals.com",
    "cje.net.cn",
    "*.holoviz.org",
    "elib.dlr.de",
    "tallinzen.net",
    "fardapaper.ir",
    "*.graph.qq.com",
    "pypi.org",
    "naec.org.uk",
    "repositorio.ipcb.pt",
    "*.googleapis.com",
    "zz.bdstatic.com",
    "iris.uniroma1.it",
    "*.readthedocs.org",
    "revistafesahancccal.org",
    "repositorio.unesp.br",
    "repositorio.uteq.edu.ec",
    "repository.kulib.kyoto-u.ac.jp",
    "*.mlr-org.com",
    "nuxt.com",
    "edepot.wur.nl",
    "*.clemson.edu",
    "cs.cornell.edu",
    "*.mmstat.com",
    "research.google",
    "smujo.id",
    "people.cs.uct.ac.za",
    "live.com",
    "udrc.eng.ed.ac.uk",
    "ceeol.com",
    "riunet.upv.es",
    "ieee-ims.org",
    "covert.io",
    "*.itch.io",
    "*.readthedocs.io",
    "ink.library.smu.edu.sg",
    "*.researchcommons.org",
    "nopr.niscpr.res.in",
    "doc.ic.ac.uk",
    "*.9game.cn",
    "eprints.utm.my",
    "pages.cs.wisc.edu",
    "e-tarjome.com",
    "nwr.gov.cn",
    "msftconnecttest.com",
    "repository.library.noaa.gov",
    "*.gyan.dev",
    "bsapubs.onlinelibrary.wiley.com",
    "search.proquest.com",
    "ecoagri.ac.cn",
    "*.privado.ai",
    "rodconnolly.com",
    "tud.qucosa.de",
    "openreview.net",
    "webextension.org",
    "mdpi.com",
    "ruor.uottawa.ca",
    "er.chdtu.edu.ua",
    "ias.ac.in",
    "python.org",
    "researchonline.gcu.ac.uk",
    "assets-eu.researchsquare.com",
    "*.msftconnecttest.com",
    "analises-ecologicas.com",
    "*.xarray.dev",
    "www-ai.ijs.si",
    "scholarpedia.org",
    "developer.android.com",
    "*.kaggleusercontent.com",
    "journals.openedition.org",
    "journal.iba-suk.edu.pk",
    "bodden.de",
    "helper.ipam.ucla.edu",
    "tobias-lib.ub.uni-tuebingen.de",
    "research.rug.nl",
    "pure.york.ac.uk",
    "aslopubs.onlinelibrary.wiley.com",
    "research.google.com",
    "yuque.com",
    "indianjournals.com",
    "iopscience.iop.org",
    "resjournals.onlinelibrary.wiley.com",
    "cirlmemphis.com",
    "*.springernature.com",
    "eprints.whiterose.ac.uk",
    "w3.mi.parisdescartes.fr",
    "caislab.kaist.ac.kr",
    "academic.oup.com",
    "go.gale.com",
    "worldclim.org",
    "openai.com",
    "ojs.unikom.ac.id",
    "worldscientific.com",
    "discovery.ucl.ac.uk",
    "proceedings.mlr.press",
    "*.deno.com",
    "conbio.onlinelibrary.wiley.com",
    "bayesiancomputationbook.com",
    "politesi.polimi.it",
    "synapse.koreamed.org",
    "sidalc.net",
    "daac.ornl.gov",
    "*.sinaimg.cn",
    "nsojournals.onlinelibrary.wiley.com",
    "*.els-cdn.com",
    "novami.com",
    "*.lzu.edu.cn",
    "pubsonline.informs.org",
    "peerj.com",
    "pure.mpg.de",
    "www.npmjs.com",
    "diva-portal.org",
    "jmirs.org",
    "*.googletagmanager.com",
    "igi-global.com",
    "jne.ut.ac.ir",
    "*.audacityteam.org",
    "mecs-press.org",
    "localhost",
    "*.live.com",
    "cell.com",
    "iovs.arvojournals.org",
    "mljar.com",
    "*.25pp.com",
    "essd.copernicus.org",
    "annualreviews.org",
    "graph.qq.com",
    "reactnative.cn",
    " fourier.taobao.com",
    "archive.interconf.center",
    "philstat.org",
    "eprints.lse.ac.uk",
    "dora.lib4ri.ch",
    "*.ssrn.com",
    "*.springer.com",
    "frankxue.com",
    "alipayobjects.com",
    "elibrary.asabe.org",
    "lyellcollection.org",
    "*.cookielaw.org",
    "hal.science",
    "jastt.org",
    "hdsr.mitpress.mit.edu",
    "detectportal.firefox.com",
    "vtechworks.lib.vt.edu",
    "report.qqweb.qq.com",
    "*.chatgpt.com",
    "newjaigs.com",
    "cse.iitkgp.ac.in",
    "browser-intake-datadoghq.com",
    "*.oracle.com",
    "ir.uitm.edu.my",
    "repository.universitasbumigora.ac.id",
    "arxiv.org",
    "ee.cuhk.edu.hk",
    "library.oapen.org",
    "ieeexplore.ieee.org",
    "mednexus.org",
    "*.elsevier.com",
    "dspace.bracu.ac.bd",
    "iibajournal.org",
    "seamlessaccess.org",
    "norma.ncirl.ie",
    "*.aliapp.org",
    "infoscience.epfl.ch",
    "studiostaticassetsprod.azureedge.net",
    "h2o-release.s3.amazonaws.com",
    "nodejs.org",
    "*.pymc.io",
    "hlevkin.com",
    "digibug.ugr.es",
    "*.mlr.press",
    "researchbank.ac.nz",
    "cs.toronto.edu",
    "iasj.net",
    "techrxiv.org",
    "periodicos.ufpe.br",
    "s.gravatar.com",
    "repository.ubn.ru.nl",
    "nph.onlinelibrary.wiley.com",
    "106.54.215.74",
    "jmir.org",
    "fonts.loli.net",
    "esj-journals.onlinelibrary.wiley.com",
    "meeting.qq.com",
    "flickerfree.org",
    "accounts.google.com.np",
    "cerf.radiologie.fr",
    "builds.libav.org",
    "code.earthengine.google.com",
    "rbciamb.com.br",
    "irbis-nbuv.gov.ua",
    "xarray.dev",
    "*.kde.org",
    "*.office.com",
    "cambridge.org",
    "anapub.co.ke",
    "research.ed.ac.uk",
    "oa.upm.es",
    "pofflab.colostate.edu",
    "geospatialhealth.net",
    "chatgpt.com",
    "webapps.fhsu.edu",
    "compass.onlinelibrary.wiley.com",
    "kiss.kstudy.com",
    "acm.org",
    "cyberleninka.ru",
    "pptr.dev",
    "*.sciencedirectassets.com",
    "emerald.com",
    "proceedings.neurips.cc",
    "jair.org",
    "krex.k-state.edu",
    "*.aliyun.com",
    "ijcsrr.org",
    "mc-stan.org",
    "wiredspace.wits.ac.za",
    "ws",
    "igb.uci.edu",
    "muroran-it.repo.nii.ac.jp",
    "ngcc.cn",
    "corinne-vacher.com",
    "kresttechnology.com",
    "*.uclouvain.be",
    "research.bangor.ac.uk",
    "*.torontomu.ca",
    "*.iop.org",
    "inderscienceonline.com",
    "reabic.net",
    "lavaan.org",
    "tensorflow-dot-devsite-v2-prod-3p.appspot.com",
    "music.163.com",
    "raw.githubusercontent.com",
    "amt.copernicus.org",
    "*.sonaliyadav.workers.dev",
    "journals.riverpublishers.com",
    "indico.ifj.edu.pl",
    "cmake.org",
    "files.eric.ed.gov",
    "iaees.org",
    "repository.law.indiana.edu",
    "dergipark.org.tr",
    "journals.sfu.ca",
    "*.ieee.org",
    "thelancet.com",
    "*.sun.ac.za",
    "meetingorganizer.copernicus.org",
    "scholarworks.umt.edu",
    "qzapp.qlogo.cn",
    "analyticalsciencejournals.onlinelibrary.wiley.com",
    "gfzpublic.gfz-potsdam.de",
    "biorxiv.org",
    "*.sagepub.com",
    "*.wandoujia.com",
    "imgcache.qq.com",
    "*.biomedcentral.com",
    "data.ornldaac.earthdata.nasa.gov",
    "unpkg.com",
    "erj.ersjournals.com",
    "s3.ca-central-1.amazonaws.com",
    "sto.nato.int",
    "*.gradle.org",
    "ise.ncsu.edu",
    "selenium.dev",
    "researchportal.bath.ac.uk",
    "isprs-archives.copernicus.org",
    "apsnet.org",
    "*.wiley.com",
    "easy.dans.knaw.nl",
    "jmes.humg.edu.vn",
    "mercurial-scm.org",
    "deno.com",
    "file.fouladi.ir",
    "*.esri.com",
    "*.52pojie.cn",
    "plausible.io",
    "*.posit.co",
    "researchonline.ljmu.ac.uk",
    "eprints.gla.ac.uk",
    "bakerlab.org",
    "croris.hr",
    "research-portal.uu.nl",
    "tc.copernicus.org",
    "*.torproject.org",
    "ion.org",
    "repositorio.ufsc.br",
    "publish.csiro.au",
    "perpustakaan.atmaluhur.ac.id",
    "dlsu.edu.ph",
    "scraperapi.com",
    "*.mail.qq.com",
    "matec-conferences.org",
    "biomedicaljour.com",
    "*.visualwebsiteoptimizer.com",
    "ceur-ws.org",
    "*.ansfoundation.org",
    "lib.baomitu.com",
    "projectpythia.org",
    "awesome-poetry.top",
    "ueaeprints.uea.ac.uk",
    "sendimage.whu.edu.cn",
    "nrl.northumbria.ac.uk",
    "pydub.com",
    "journals.lww.com",
    "scijournals.onlinelibrary.wiley.com",
    "hcjournal.org",
    "joss.theoj.org",
    "nature.com",
    "osgeo.org",
    "cloudflare.com",
    "witpress.com",
    "felipebravom.com",
    "pdfs.semanticscholar.org",
    "doi.org",
    "*.jquery.com",
    "*.r-project.org",
    "hess.copernicus.org",
    "openresearch.surrey.ac.uk",
    "jae-tech.com",
    "zslpublications.onlinelibrary.wiley.com",
    "aitskadapa.ac.in",
    "link.springer.com",
    "*.github.io",
    "cgspace.cgiar.org",
    "openaccess.thecvf.com",
    "eartharxiv.org",
    "sscdigitalstorytelling.pbworks.com",
    "digitalcommons.usu.edu",
    "electronjs.org",
    "medrxiv.org",
    "elifesciences.org",
    "core.ac.uk",
    "int-res.com",
    "www.wjx.cn",
    "*.weixin.qq.com",
    "qmro.qmul.ac.uk",
    "koreascience.kr",
    "*.hsforms.net",
    "scis.scichina.com",
    "*.neea.edu.cn",
    "*.yeepay.com",
    "physicamedica.com",
    "aaai.org",
    "pnas.org",
    "fs.usda.gov",
    "journal-dogorangsang.in",
    "10.10.0.166",
    "aegis.qq.com",
    "tristan.cordier.free.fr",
    "*.riskified.com",
    "*.r-lib.org",
    "*.conicet.gov.ar",
    "assets.pubpub.org",
    "eprint.iacr.org",
    "js.trendmd.com",
    "mail.qq.com",
    "reproducible-builds.org",
    "europepmc.org",
    "mce.biophys.msu.ru",
    "tensorflow.org",
    "aapm.onlinelibrary.wiley.com",
    "scholarbank.nus.edu.sg",
    "ajemb.us",
    "frontiersin.org",
    "epubs.siam.org",
    "api.taylorfrancis.com",
    "b-cubed.eu",
    "oup.silverchair-cdn.com",
    "scirp.org",
    "indexinvestorportfolios.com",
    "ojs.aaai.org",
    "d-nb.info",
    "cit.ctu.edu.vn",
    "onepetro.org",
    "dspace.aztidata.es",
    "pyro.ai"
];