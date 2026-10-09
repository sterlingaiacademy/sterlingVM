import os

path = r'c:\anti\sterlingVM\src\app\dashboard\analytics\page.tsx'
with open(path, 'r', encoding='utf-8') as f:
    content = f.read()

# Add states for IG Posts
content = content.replace('const [isLoading, setIsLoading] = useState(true);', '''const [isLoading, setIsLoading] = useState(true);
  const [igPosts, setIgPosts] = useState<any[]>([]);
  const [igLoading, setIgLoading] = useState(false);''')

# Fetch IG Posts
content = content.replace('      setIsLoading(false);\n    }\n  };', '''      setIsLoading(false);
    }
  };

  const fetchIgPosts = async () => {
    setIgLoading(true);
    try {
      const res = await fetch('/api/meta/analytics/ig-posts');
      if (res.ok) {
        const data = await res.json();
        if (data.data) {
          setIgPosts(data.data);
        }
      }
    } catch (e) {
      console.error(e);
    } finally {
      setIgLoading(false);
    }
  };
  
  useEffect(() => {
    fetchIgPosts();
  }, []);
''')

# Add IG Posts UI below WhatsApp Funnel
insertion = '''          {/* INSTAGRAM POST PERFORMANCE */}
          <div className="bg-white dark:bg-[#050505] p-8 rounded-3xl shadow-sm border border-gray-100 dark:border-white/5 animate-fade-up" style={{ animationDelay: '0.2s' }}>
            <div className="flex items-center justify-between mb-8">
              <h3 className="text-xs font-black uppercase tracking-widest text-gray-400 flex items-center gap-2">
                <div className="w-2 h-2 rounded-full bg-pink-500 animate-pulse" />
                Instagram Post Performance
              </h3>
              <button 
                onClick={fetchIgPosts}
                disabled={igLoading}
                className="px-4 py-2 bg-pink-50 dark:bg-pink-900/10 text-pink-600 rounded-lg text-[10px] font-bold uppercase tracking-widest hover:bg-pink-100 dark:hover:bg-pink-900/20 transition-colors disabled:opacity-50"
              >
                {igLoading ? "Fetching..." : "Refresh"}
              </button>
            </div>
            
            <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">
              {igPosts.length === 0 && !igLoading && (
                <div className="col-span-full py-12 text-center text-gray-400 text-sm">
                  No Instagram posts found. Make sure your Instagram Account ID is configured.
                </div>
              )}
              {igPosts.map((post: any) => (
                <a key={post.id} href={post.permalink} target="_blank" rel="noreferrer" className="group block bg-gray-50 dark:bg-black/50 rounded-2xl overflow-hidden border border-gray-100 dark:border-white/5 hover:border-pink-500/30 transition-all">
                  <div className="aspect-square bg-gray-200 dark:bg-white/5 relative overflow-hidden">
                    {(post.media_type === 'IMAGE' || post.media_type === 'CAROUSEL_ALBUM') && (
                      <img src={post.media_url} alt="" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                    )}
                    {post.media_type === 'VIDEO' && (
                      <>
                        <img src={post.thumbnail_url || post.media_url} alt="" className="w-full h-full object-cover group-hover:scale-105 transition-transform duration-500" />
                        <div className="absolute inset-0 flex items-center justify-center bg-black/20">
                          <div className="w-8 h-8 rounded-full bg-white/30 backdrop-blur flex items-center justify-center">
                            <div className="w-0 h-0 border-t-4 border-l-6 border-b-4 border-transparent border-l-white ml-1" />
                          </div>
                        </div>
                      </>
                    )}
                  </div>
                  <div className="p-4">
                    <p className="text-xs text-gray-600 dark:text-gray-300 line-clamp-2 mb-3">{post.caption || "No caption"}</p>
                    <div className="flex items-center justify-between text-[10px] font-black uppercase text-gray-400">
                      <span className="flex items-center gap-1"><span className="text-pink-500">?</span> {post.like_count}</span>
                      <span className="flex items-center gap-1">?? {post.comments_count}</span>
                    </div>
                  </div>
                </a>
              ))}
            </div>
          </div>
'''

content = content.replace('''          {/* WHATSAPP BROADCAST FUNNEL */}''', insertion + '\n          {/* WHATSAPP BROADCAST FUNNEL */}')

with open(path, 'w', encoding='utf-8') as f:
    f.write(content)
