import os

path = r'c:\anti\sterlingVM\src\app\dashboard\campaigns\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add states
content = content.replace('const [igCaption, setIgCaption] = useState(', '''const [useTemplate, setUseTemplate] = useState(false);
  const [templateName, setTemplateName] = useState("");
  const [templateLang, setTemplateLang] = useState("en");
  
  const [igCaption, setIgCaption] = useState(''')

# Update handlePush
content = content.replace('''      const res = await fetch("/api/meta/campaign/push", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          phoneNumbers,
          adBody,
          adFooter,
          buttonText,
          buttonUrl,
          imageBlob
        })
      });''', '''      const res = await fetch("/api/meta/campaign/push", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({
          phoneNumbers,
          adBody,
          adFooter,
          buttonText,
          buttonUrl,
          imageBlob,
          useTemplate,
          templateName,
          templateLang
        })
      });''')

# Add Template Toggle UI
insertion = '''            </div>

            {/* MESSAGE TYPE TOGGLE */}
            <div className="flex items-center gap-4 bg-gray-50 dark:bg-black/30 p-2 rounded-xl mb-6 border border-gray-100 dark:border-white/5 w-max">
              <button 
                onClick={() => setUseTemplate(false)}
                className={px-4 py-2 rounded-lg text-xs font-bold uppercase tracking-widest transition-all }
              >
                Standard
              </button>
              <button 
                onClick={() => setUseTemplate(true)}
                className={px-4 py-2 rounded-lg text-xs font-bold uppercase tracking-widest transition-all flex items-center gap-2 }
              >
                Template
                <span className="bg-purple-100 text-purple-600 dark:bg-black/50 dark:text-purple-300 px-2 py-0.5 rounded-full text-[9px]">PRO</span>
              </button>
            </div>

            {useTemplate ? (
              <div className="mb-6 animate-fade-up">
                <div className="bg-purple-50 dark:bg-purple-900/10 border border-purple-100 dark:border-purple-500/20 p-6 rounded-3xl">
                  <h4 className="text-xs font-black uppercase tracking-widest text-purple-600 dark:text-purple-400 mb-4 flex items-center gap-2">
                    <MessageCircle className="w-4 h-4" />
                    Template Configuration
                  </h4>
                  <div className="grid grid-cols-2 gap-4">
                    <div>
                      <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Template Name</label>
                      <input 
                        type="text" 
                        value={templateName}
                        onChange={(e) => setTemplateName(e.target.value)}
                        placeholder="e.g. sebi_video_demo" 
                        className="w-full bg-white dark:bg-[#050505] border border-gray-200 dark:border-white/10 py-3 px-4 rounded-2xl text-sm focus:outline-none focus:border-purple-600 transition-colors"
                      />
                    </div>
                    <div>
                      <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Language Code</label>
                      <input 
                        type="text" 
                        value={templateLang}
                        onChange={(e) => setTemplateLang(e.target.value)}
                        placeholder="e.g. en" 
                        className="w-full bg-white dark:bg-[#050505] border border-gray-200 dark:border-white/10 py-3 px-4 rounded-2xl text-sm focus:outline-none focus:border-purple-600 transition-colors"
                      />
                    </div>
                  </div>
                  <p className="text-[10px] text-gray-500 mt-4 leading-relaxed font-medium">
                    Enter the exact name of the approved template from your Meta WhatsApp Manager. If your template has a media header, upload your image/video in the banner box above and it will automatically be attached! The template's actual text and buttons are pulled directly from Meta, so you don't need to type them here.
                  </p>
                </div>
              </div>
            ) : (
              <>
                <div className="mb-6 animate-fade-up">
'''

content = content.replace('''            </div>

            <div className="mb-6">''', insertion)

# Close the fragment
content = content.replace('''              <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Redirect URL</label>''', '''              <label className="block text-[10px] font-black uppercase tracking-widest text-gray-400 mb-2 pl-2">Redirect URL</label>''')

content = content.replace('''                  </div>
                </div>
              </div>
            </div>''', '''                  </div>
                </div>
              </div>
              </>
            )}
            </div>''')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
