<!DOCTYPE html>
<html lang="vi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
 
    <script src="https://cdn.tailwindcss.com"></script>
    <link href="https://fonts.googleapis.com/css2?family=Playfair+Display:ital,wght@0,400;0,600;0,700;1,400&family=Lato:wght@300;400;700&display=swap" rel="stylesheet">
    <link rel="stylesheet" href="https://cdnjs.cloudflare.com/ajax/libs/font-awesome/6.4.0/css/all.min.css">
    
    <script>
        tailwind.config = {
            theme: {
                extend: {
                    colors: {
                        gold: {
                            DEFAULT: '#D4AF37',
                            light: '#F3E5AB',
                            dark: '#AA8C2C',
                        },
                        dark: {
                            DEFAULT: '#111111',
                            card: '#1A1A1A',
                        }
                    },
                    fontFamily: {
                        serif: ['"Playfair Display"', 'serif'],
                        sans: ['Lato', 'sans-serif'],
                    }
                }
            }
        }
    </script>
    <style>
        body {
            background-color: #111111;
            color: #f1f1f1;
            scroll-behavior: smooth;
        }
        .text-gradient-gold {
            background: linear-gradient(to right, #D4AF37, #F3E5AB, #D4AF37);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }
        .border-gold-gradient {
            border-image: linear-gradient(to right, #D4AF37, #AA8C2C) 1;
        }
        /* Custom Scrollbar */
        ::-webkit-scrollbar {
            width: 8px;
        }
        ::-webkit-scrollbar-track {
            background: #111;
        }
        ::-webkit-scrollbar-thumb {
            background: #D4AF37;
            border-radius: 4px;
        }
        .menu-item-hover:hover .add-to-cart-btn {
            opacity: 1;
            transform: translateY(0);
        }
        .add-to-cart-btn {
            opacity: 0;
            transform: translateY(10px);
            transition: all 0.3s ease;
        }
        /* Modal transitions */
        .modal-enter { opacity: 0; }
        .modal-enter-active { opacity: 1; transition: opacity 300ms; }
        .modal-exit { opacity: 1; }
        .modal-exit-active { opacity: 0; transition: opacity 300ms; }
    </style>
</head>
<body class="font-sans antialiased overflow-x-hidden">

    <nav class="fixed w-full z-50 bg-dark/90 backdrop-blur-md border-b border-gold/20 transition-all duration-300" id="navbar">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between items-center h-20">
                <div class="flex-shrink-0 flex items-center">
                    <a href="#" class="font-serif text-3xl font-bold text-gradient-gold tracking-wider">L'AURA</a>
                </div>
                <div class="hidden md:flex space-x-8 items-center">
                    <a href="#home" class="text-gray-300 hover:text-gold transition-colors duration-200">Trang Chủ</a>
                    <a href="#about" class="text-gray-300 hover:text-gold transition-colors duration-200">Không Gian</a>
                    <a href="#menu" class="text-gray-300 hover:text-gold transition-colors duration-200">Thực Đơn</a>
                    <a href="#reservation" class="text-gray-300 hover:text-gold transition-colors duration-200">Đặt Bàn</a>
                    <button onclick="toggleCart()" class="relative text-gold hover:text-gold-light transition-colors">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span id="cart-count" class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">0</span>
                    </button>
                </div>
                <!-- Mobile menu button -->
                <div class="md:hidden flex items-center">
                    <button onclick="toggleCart()" class="relative text-gold mr-4">
                        <i class="fas fa-shopping-bag text-xl"></i>
                        <span id="mobile-cart-count" class="absolute -top-2 -right-2 bg-red-500 text-white text-xs font-bold rounded-full h-5 w-5 flex items-center justify-center">0</span>
                    </button>
                    <button id="mobile-menu-btn" class="text-gray-300 hover:text-gold focus:outline-none">
                        <i class="fas fa-bars text-2xl"></i>
                    </button>
                </div>
            </div>
        </div>
        <!-- Mobile Menu -->
        <div id="mobile-menu" class="hidden md:hidden bg-dark-card border-b border-gold/20">
            <div class="px-2 pt-2 pb-3 space-y-1 sm:px-3">
                <a href="#home" class="block px-3 py-2 text-gray-300 hover:text-gold">Trang Chủ</a>
                <a href="#about" class="block px-3 py-2 text-gray-300 hover:text-gold">Không Gian</a>
                <a href="#menu" class="block px-3 py-2 text-gray-300 hover:text-gold">Thực Đơn</a>
                <a href="#reservation" class="block px-3 py-2 text-gray-300 hover:text-gold">Đặt Bàn</a>
            </div>
        </div>
    </nav>

    <section id="home" class="relative h-screen flex items-center justify-center">
        <div class="absolute inset-0 z-0">
            <img src="https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=2070&auto=format&fit=crop" alt="Restaurant Interior" class="w-full h-full object-cover opacity-40">
            <div class="absolute inset-0 bg-gradient-to-b from-dark/60 via-dark/40 to-dark"></div>
        </div>
        <div class="relative z-10 text-center px-4 max-w-4xl mx-auto mt-16">
            <h2 class="text-gold tracking-widest uppercase text-sm font-bold mb-4">Trải nghiệm ẩm thực đỉnh cao</h2>
            <h1 class="font-serif text-5xl md:text-7xl font-bold mb-6 leading-tight text-gradient-gold">Hương Vị Của<br>Sự Hoàn Mỹ</h1>
            <p class="text-gray-300 text-lg md:text-xl mb-10 font-light max-w-2xl mx-auto">Đánh thức mọi giác quan với không gian sang trọng và những món ăn được chế tác tỉ mỉ bởi các siêu đầu bếp Michelin.</p>
            <a href="#reservation" class="inline-block border-2 border-gold text-gold hover:bg-gold hover:text-dark px-8 py-3 uppercase tracking-wider font-bold transition-all duration-300">Đặt bàn ngay</a>
        </div>
    </section>

    <section id="about" class="py-24 bg-dark">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="flex flex-col md:flex-row items-center gap-16">
                <div class="md:w-1/2">
                    <div class="relative">
                        <img src="https://images.unsplash.com/photo-1550966871-3ed3cdb5ed0c?q=80&w=2070&auto=format&fit=crop" alt="Fine Dining" class="w-full h-[500px] object-cover rounded-sm">
                        <div class="absolute -bottom-8 -right-8 w-48 h-48 border-2 border-gold z-0 hidden md:block"></div>
                    </div>
                </div>
                <div class="md:w-1/2">
                    <h3 class="font-serif text-4xl mb-6 text-white"><span class="text-gold">Không gian</span> thượng lưu</h3>
                    <p class="text-gray-400 leading-relaxed mb-6">
                        Tọa lạc tại tầng cao nhất của trung tâm thành phố, L'AURA mang đến tầm nhìn toàn cảnh tuyệt đẹp. Nội thất được thiết kế kết hợp giữa vẻ đẹp cổ điển châu Âu và nét hiện đại, tối giản.
                    </p>
                    <p class="text-gray-400 leading-relaxed mb-8">
                        Mỗi góc nhỏ tại L'AURA đều được chăm chút kỹ lưỡng với ánh sáng dịu nhẹ, âm nhạc du dương và sự riêng tư tuyệt đối, tạo nên bầu không khí lãng mạn và đẳng cấp cho những buổi tiệc đặc biệt của bạn.
                    </p>
                    <div class="flex items-center space-x-8">
                        <div>
                            <p class="text-gold font-serif text-3xl">5★</p>
                            <p class="text-xs text-gray-500 uppercase tracking-wider">Tiêu chuẩn</p>
                        </div>
                        <div>
                            <p class="text-gold font-serif text-3xl">3</p>
                            <p class="text-xs text-gray-500 uppercase tracking-wider">Sao Michelin</p>
                        </div>
                    </div>
                </div>
            </div>
        </div>
    </section>

    <section id="menu" class="py-24 bg-dark-card border-y border-gold/10">
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
            <div class="text-center mb-16">
                <h2 class="text-gold tracking-widest uppercase text-sm font-bold mb-2">Khám phá</h2>
                <h3 class="font-serif text-4xl text-white">Thực Đơn Hảo Hạng</h3>
            </div>
            
            <!-- Menu Tabs -->
            <div class="flex justify-center space-x-8 mb-12 border-b border-gray-800 pb-4">
                <button onclick="switchTab('food')" id="tab-food" class="text-gold font-bold uppercase tracking-wider border-b-2 border-gold pb-2 transition-all">Món Ăn</button>
                <button onclick="switchTab('drinks')" id="tab-drinks" class="text-gray-500 hover:text-gray-300 font-bold uppercase tracking-wider pb-2 transition-all border-b-2 border-transparent">Thức Uống</button>
            </div>

            <!-- Menu Grid -->
            <div id="menu-container" class="grid grid-cols-1 md:grid-cols-2 gap-x-12 gap-y-10">
                <!-- Items will be injected here via JS -->
            </div>
        </div>
    </section>

    <section id="reservation" class="py-24 bg-dark relative">
        <div class="max-w-4xl mx-auto px-4 sm:px-6 lg:px-8 relative z-10">
            <div class="bg-dark-card p-8 md:p-12 border border-gold/20 shadow-2xl">
                <div class="text-center mb-10">
                    <h3 class="font-serif text-3xl text-white mb-2">Đặt Bàn</h3>
                    <p class="text-gray-400 text-sm">Vui lòng điền thông tin để chúng tôi chuẩn bị đón tiếp tốt nhất.</p>
                </div>
                <form id="reservation-form" class="space-y-6">
                    <div class="grid grid-cols-1 md:grid-cols-2 gap-6">
                        <div>
                            <label class="block text-xs text-gold uppercase tracking-wider mb-2">Họ và Tên</label>
                            <input type="text" id="res-name" required class="w-full bg-transparent border-b border-gray-600 focus:border-gold text-white py-2 outline-none transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs text-gold uppercase tracking-wider mb-2">Số Điện Thoại</label>
                            <input type="tel" id="res-phone" required class="w-full bg-transparent border-b border-gray-600 focus:border-gold text-white py-2 outline-none transition-colors">
                        </div>
                        <div>
                            <label class="block text-xs text-gold uppercase tracking-wider mb-2">Ngày</label>
                            <input type="date" id="res-date" required class="w-full bg-transparent border-b border-gray-600 focus:border-gold text-white py-2 outline-none transition-colors style-date">
                        </div>
                        <div>
                            <label class="block text-xs text-gold uppercase tracking-wider mb-2">Giờ</label>
                            <select id="res-time" required class="w-full bg-dark border-b border-gray-600 focus:border-gold text-white py-2 outline-none transition-colors">
                                <option value="18:00">18:00</option>
                                <option value="19:00">19:00</option>
                                <option value="20:00">20:00</option>
                                <option value="21:00">21:00</option>
                            </select>
                        </div>
                        <div>
                            <label class="block text-xs text-gold uppercase tracking-wider mb-2">Số Người</label>
                            <input type="number" id="res-guests" min="1" max="20" required class="w-full bg-transparent border-b border-gray-600 focus:border-gold text-white py-2 outline-none transition-colors">
                        </div>
                    </div>
                    <div>
                        <label class="block text-xs text-gold uppercase tracking-wider mb-2">Ghi chú đặc biệt (Tùy chọn)</label>
                        <textarea id="res-notes" rows="2" class="w-full bg-transparent border-b border-gray-600 focus:border-gold text-white py-2 outline-none transition-colors"></textarea>
                    </div>
                    <div class="pt-4 text-center">
                        <button type="submit" id="btn-reserve" class="bg-gold text-dark font-bold uppercase tracking-wider py-3 px-10 hover:bg-gold-light transition-colors w-full md:w-auto">Xác nhận đặt bàn</button>
                    </div>
                </form>
            </div>
        </div>
    </section>

    <!-- Cart Sidebar Overlay -->
    <div id="cart-overlay" class="fixed inset-0 bg-black/70 z-[60] hidden transition-opacity duration-300 opacity-0" onclick="if(event.target === this) toggleCart()">
        <div id="cart-sidebar" class="absolute top-0 right-0 h-full w-full md:w-[450px] bg-dark-card border-l border-gold/20 shadow-2xl transform translate-x-full transition-transform duration-300 flex flex-col">
            <!-- Header -->
            <div class="p-6 border-b border-gray-800 flex justify-between items-center bg-dark">
                <h2 class="font-serif text-2xl text-gold">Đơn Hàng Của Bạn</h2>
                <button onclick="toggleCart()" class="text-gray-400 hover:text-white transition-colors">
                    <i class="fas fa-times text-xl"></i>
                </button>
            </div>
            
            <!-- Cart Items -->
            <div id="cart-items-container" class="flex-1 overflow-y-auto p-6 space-y-6">
                <!-- Cart items will be rendered here -->
                <div class="text-center text-gray-500 mt-10 hidden" id="empty-cart-msg">Giỏ hàng của bạn đang trống.</div>
            </div>
            
            <!-- Footer / Checkout -->
            <div class="p-6 border-t border-gray-800 bg-dark">
                <div class="flex justify-between items-center mb-6">
                    <span class="text-gray-400">Tổng cộng:</span>
                    <span id="cart-total" class="font-serif text-2xl text-white">0 ₫</span>
                </div>
                
                <!-- Payment Method Selection -->
                <div class="mb-6">
                    <label class="block text-xs text-gold uppercase tracking-wider mb-3">Phương thức thanh toán</label>
                    <div class="grid grid-cols-3 gap-2">
                        <label class="cursor-pointer">
                            <input type="radio" name="payment" value="momo" class="peer hidden" checked>
                            <div class="border border-gray-700 rounded p-2 text-center peer-checked:border-gold peer-checked:bg-gold/10 transition-all">
                                <img src="https://upload.wikimedia.org/wikipedia/vi/f/fe/MoMo_Logo.png" alt="MoMo" class="h-6 mx-auto mb-1">
                                <span class="text-[10px] text-gray-300">MoMo</span>
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="radio" name="payment" value="zalopay" class="peer hidden">
                            <div class="border border-gray-700 rounded p-2 text-center peer-checked:border-gold peer-checked:bg-gold/10 transition-all">
                                <span class="text-blue-500 font-bold text-sm block mb-1 leading-6">ZaloPay</span>
                                <span class="text-[10px] text-gray-300">ZaloPay</span>
                            </div>
                        </label>
                        <label class="cursor-pointer">
                            <input type="radio" name="payment" value="card" class="peer hidden">
                            <div class="border border-gray-700 rounded p-2 text-center peer-checked:border-gold peer-checked:bg-gold/10 transition-all">
                                <i class="fas fa-credit-card text-gray-400 text-lg block mb-1 leading-6"></i>
                                <span class="text-[10px] text-gray-300">Thẻ Visa/Master</span>
                            </div>
                        </label>
                    </div>
                </div>
                
                <button id="btn-checkout" onclick="processCheckout()" class="w-full bg-gold text-dark font-bold py-3 uppercase tracking-wider hover:bg-gold-light transition-colors disabled:opacity-50 disabled:cursor-not-allowed">
                    Thanh Toán
                </button>
            </div>
        </div>
    </div>

    <!-- Custom Toast Notification -->
    <div id="toast-container" class="fixed bottom-5 right-5 z-[70] flex flex-col gap-2"></div>

    <footer class="bg-black py-12 border-t border-gold/10">
        <div class="max-w-7xl mx-auto px-4 text-center">
            <h2 class="font-serif text-2xl font-bold text-gold mb-6">L'AURA</h2>
            <div class="flex justify-center space-x-6 mb-8">
                <a href="#" class="text-gray-500 hover:text-gold transition-colors"><i class="fab fa-facebook-f"></i></a>
                <a href="#" class="text-gray-500 hover:text-gold transition-colors"><i class="fab fa-instagram"></i></a>
                <a href="#" class="text-gray-500 hover:text-gold transition-colors"><i class="fab fa-tripadvisor"></i></a>
            </div>
            <p class="text-gray-600 text-sm">© 2026 L'Aura Fine Dining. All rights reserved.</p>
        </div>
    </footer>

    <script type="module">
        import { initializeApp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-app.js";
        import { getAuth, signInAnonymously, signInWithCustomToken, onAuthStateChanged } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-auth.js";
        import { getFirestore, collection, addDoc, serverTimestamp } from "https://www.gstatic.com/firebasejs/11.6.1/firebase-firestore.js";

        // Firebase Setup using environment variables
        const appId = typeof __app_id !== 'undefined' ? __app_id : 'laura-restaurant-demo';
        let firebaseConfig;
        
        try {
            firebaseConfig = typeof __firebase_config !== 'undefined' ? JSON.parse(__firebase_config) : {
                // Dummy config for fallback if needed, though env should provide it
                apiKey: "demo-key",
                projectId: "demo-project"
            };
        } catch (e) {
            console.error("Firebase config error:", e);
        }

        const app = initializeApp(firebaseConfig);
        const db = getFirestore(app);
        const auth = getAuth(app);
        let currentUser = null;

        // Strict Auth Flow
        const initAuth = async () => {
            try {
                if (typeof __initial_auth_token !== 'undefined' && __initial_auth_token) {
                    await signInWithCustomToken(auth, __initial_auth_token);
                } else {
                    await signInAnonymously(auth);
                }
            } catch (error) {
                console.error("Auth Error:", error);
                showToast("Lỗi xác thực hệ thống.", "error");
            }
        };

        onAuthStateChanged(auth, (user) => {
            if (user) {
                currentUser = user;
                console.log("User authenticated:", user.uid);
            }
        });

        // Initialize auth immediately
        initAuth();

        // Make Firebase functions available globally for inline handlers if needed
        window.db = db;
        window.currentUser = currentUser;
        window.appId = appId;
        window.addDoc = addDoc;
        window.collection = collection;
        window.serverTimestamp = serverTimestamp;

        // Handle Reservation Submit
        document.getElementById('reservation-form').addEventListener('submit', async (e) => {
            e.preventDefault();
            const btn = document.getElementById('btn-reserve');
            const originalText = btn.innerText;
            
            if (!auth.currentUser) {
                showToast("Đang kết nối hệ thống. Vui lòng thử lại sau giây lát.", "error");
                return;
            }

            const resData = {
                name: document.getElementById('res-name').value,
                phone: document.getElementById('res-phone').value,
                date: document.getElementById('res-date').value,
                time: document.getElementById('res-time').value,
                guests: parseInt(document.getElementById('res-guests').value),
                notes: document.getElementById('res-notes').value,
                status: 'pending',
                createdAt: serverTimestamp()
            };

            try {
                btn.innerText = "Đang xử lý...";
                btn.disabled = true;

                // RULE 1: Strict paths applied here
                const reservationsRef = collection(db, 'artifacts', appId, 'users', auth.currentUser.uid, 'reservations');
                await addDoc(reservationsRef, resData);
                
                showToast("Đặt bàn thành công! Chúng tôi sẽ liên hệ sớm để xác nhận.", "success");
                e.target.reset();
            } catch (error) {
                console.error("Error adding reservation:", error);
                showToast("Đã xảy ra lỗi. Vui lòng thử lại sau.", "error");
            } finally {
                btn.innerText = originalText;
                btn.disabled = false;
            }
        });

        // Expose checkout function to global scope to be called by onclick
        window.processCheckout = async function() {
            if (cart.length === 0) return;
            if (!auth.currentUser) {
                showToast("Hệ thống chưa sẵn sàng. Vui lòng đợi.", "error");
                return;
            }

            const btn = document.getElementById('btn-checkout');
            const originalText = btn.innerText;
            btn.innerText = "Đang xử lý...";
            btn.disabled = true;

            const selectedPayment = document.querySelector('input[name="payment"]:checked').value;
            
            const orderData = {
                items: cart,
                totalAmount: cart.reduce((sum, item) => sum + (item.price * item.quantity), 0),
                paymentMethod: selectedPayment,
                status: 'paid',
                createdAt: serverTimestamp()
            };

            try {
                // RULE 1: Strict Paths
                const ordersRef = collection(db, 'artifacts', appId, 'users', auth.currentUser.uid, 'orders');
                await addDoc(ordersRef, orderData);
                
                cart = [];
                updateCartUI();
                toggleCart();
                
                // Simulate payment redirect/success
                setTimeout(() => {
                    showToast(`Thanh toán thành công qua ${selectedPayment.toUpperCase()}!`, "success");
                }, 500);

            } catch (error) {
                console.error("Order error:", error);
                showToast("Lỗi thanh toán. Vui lòng thử lại.", "error");
            } finally {
                btn.innerText = originalText;
                btn.disabled = false;
            }
        }
    </script>

    <script>
        // Data Structure
        const menuData = {
            food: [
                { id: 'f1', name: 'Bò Wagyu A5 Steak', desc: 'Thăn ngoại bò Wagyu A5 nhập khẩu Nhật Bản, nướng than hoa ăn kèm nấm Truffle.', price: 2500000, img: 'https://images.unsplash.com/photo-1544025162-8111f4a76154?q=80&w=1500&auto=format&fit=crop' },
                { id: 'f2', name: 'Tôm Hùm Thermidor', desc: 'Tôm hùm Pháp sốt kem phô mai Gruyère đút lò, phục vụ cùng măng tây.', price: 1800000, img: 'https://images.unsplash.com/photo-1625937751876-4515cd8e78db?q=80&w=1500&auto=format&fit=crop' },
                { id: 'f3', name: 'Gan Ngỗng Áp Chảo', desc: 'Foie gras Pháp áp chảo hoàn hảo, mứt sung và bánh mì brioche.', price: 950000, img: 'https://images.unsplash.com/photo-1582170327334-a08ce1eefb59?q=80&w=1500&auto=format&fit=crop' },
                { id: 'f4', name: 'Sò Điệp Hokkaido Hokkaido', desc: 'Sò điệp Nhật Bản áp chảo, sốt bơ chanh và trứng cá caviar.', price: 850000, img: 'https://images.unsplash.com/photo-1626200926732-44675b3fd4b6?q=80&w=1500&auto=format&fit=crop' }
            ],
            drinks: [
                { id: 'd1', name: 'Dom Pérignon Vintage', desc: 'Champagne cao cấp với hương vị tinh tế của trái cây trắng và bánh mì nướng.', price: 8500000, img: 'https://images.unsplash.com/photo-1584916201218-f4242ceb4809?q=80&w=1500&auto=format&fit=crop' },
                { id: 'd2', name: 'Château Margaux 2015', desc: 'Rượu vang đỏ đê mê từ Bordeaux, Pháp, đậm đà và cấu trúc hoàn hảo.', price: 12000000, img: 'https://images.unsplash.com/photo-1506377247377-2a5b3b417ebb?q=80&w=1500&auto=format&fit=crop' },
                { id: 'd3', name: 'L\'Aura Signature Cocktail', desc: 'Sự pha trộn độc bản giữa Gin, hoa sâm ngọc linh và bụi vàng 24k.', price: 450000, img: 'https://images.unsplash.com/photo-1514362545857-3bc16c4c7d1b?q=80&w=1500&auto=format&fit=crop' },
                { id: 'd4', name: 'Macallan 18 Years', desc: 'Single malt scotch whisky 18 năm tuổi, hương sherry oak đặc trưng.', price: 1500000, img: 'https://images.unsplash.com/photo-1527281400683-1aae777175f8?q=80&w=1500&auto=format&fit=crop' }
            ]
        };

        let currentTab = 'food';
        window.cart = []; // Made global for Firebase script to access

        // Utility: Format currency
        const formatMoney = (amount) => {
            return amount.toLocaleString('vi-VN') + ' ₫';
        };

        // Render Menu
        const renderMenu = () => {
            const container = document.getElementById('menu-container');
            container.innerHTML = '';
            
            menuData[currentTab].forEach(item => {
                const div = document.createElement('div');
                div.className = 'flex flex-col sm:flex-row gap-6 p-4 rounded-lg bg-dark hover:bg-black transition-colors menu-item-hover border border-transparent hover:border-gold/20';
                
                div.innerHTML = `
                    <div class="sm:w-1/3 overflow-hidden rounded">
                        <img src="${item.img}" alt="${item.name}" class="w-full h-32 object-cover transform hover:scale-110 transition-transform duration-500">
                    </div>
                    <div class="sm:w-2/3 flex flex-col justify-between">
                        <div>
                            <div class="flex justify-between items-start mb-2">
                                <h4 class="font-serif text-xl text-white">${item.name}</h4>
                                <span class="text-gold font-bold whitespace-nowrap ml-4">${formatMoney(item.price)}</span>
                            </div>
                            <p class="text-gray-500 text-sm mb-4 leading-relaxed">${item.desc}</p>
                        </div>
                        <button onclick="addToCart('${item.id}', '${currentTab}')" class="add-to-cart-btn text-left text-xs uppercase tracking-wider text-gold hover:text-white transition-colors flex items-center">
                            <i class="fas fa-plus mr-2"></i> Thêm vào đơn
                        </button>
                    </div>
                `;
                container.appendChild(div);
            });
        };

        // Switch Tabs
        window.switchTab = (tab) => {
            currentTab = tab;
            
            // Update tab styles
            document.getElementById('tab-food').className = tab === 'food' 
                ? 'text-gold font-bold uppercase tracking-wider border-b-2 border-gold pb-2 transition-all' 
                : 'text-gray-500 hover:text-gray-300 font-bold uppercase tracking-wider pb-2 transition-all border-b-2 border-transparent';
                
            document.getElementById('tab-drinks').className = tab === 'drinks' 
                ? 'text-gold font-bold uppercase tracking-wider border-b-2 border-gold pb-2 transition-all' 
                : 'text-gray-500 hover:text-gray-300 font-bold uppercase tracking-wider pb-2 transition-all border-b-2 border-transparent';
                
            renderMenu();
        };

        // Cart Logic
        window.addToCart = (id, type) => {
            const item = menuData[type].find(i => i.id === id);
            if (!item) return;

            const existingItem = cart.find(i => i.id === id);
            if (existingItem) {
                existingItem.quantity += 1;
            } else {
                cart.push({ ...item, quantity: 1 });
            }
            
            updateCartUI();
            showToast(`Đã thêm ${item.name} vào đơn hàng.`, "success");
        };

        window.updateQuantity = (id, change) => {
            const index = cart.findIndex(i => i.id === id);
            if (index > -1) {
                cart[index].quantity += change;
                if (cart[index].quantity <= 0) {
                    cart.splice(index, 1);
                }
                updateCartUI();
            }
        };

        window.updateCartUI = () => {
            // Update badges
            const totalItems = cart.reduce((sum, item) => sum + item.quantity, 0);
            document.getElementById('cart-count').innerText = totalItems;
            document.getElementById('mobile-cart-count').innerText = totalItems;
            
            // Update modal content
            const container = document.getElementById('cart-items-container');
            const emptyMsg = document.getElementById('empty-cart-msg');
            const checkoutBtn = document.getElementById('btn-checkout');
            const totalEl = document.getElementById('cart-total');
            
            container.innerHTML = '';
            
            if (cart.length === 0) {
                container.appendChild(emptyMsg);
                emptyMsg.classList.remove('hidden');
                checkoutBtn.disabled = true;
                totalEl.innerText = '0 ₫';
                return;
            }
            
            emptyMsg.classList.add('hidden');
            checkoutBtn.disabled = false;
            
            let total = 0;
            
            cart.forEach(item => {
                total += item.price * item.quantity;
                const div = document.createElement('div');
                div.className = 'flex justify-between items-center bg-dark p-3 rounded border border-gray-800';
                div.innerHTML = `
                    <div class="flex-1">
                        <h5 class="text-white text-sm font-serif mb-1 truncate">${item.name}</h5>
                        <p class="text-gold text-xs">${formatMoney(item.price)}</p>
                    </div>
                    <div class="flex items-center space-x-3 ml-4 bg-black rounded-full px-2 py-1">
                        <button onclick="updateQuantity('${item.id}', -1)" class="text-gray-400 hover:text-white focus:outline-none"><i class="fas fa-minus text-xs"></i></button>
                        <span class="text-white text-sm w-4 text-center">${item.quantity}</span>
                        <button onclick="updateQuantity('${item.id}', 1)" class="text-gray-400 hover:text-white focus:outline-none"><i class="fas fa-plus text-xs"></i></button>
                    </div>
                `;
                container.appendChild(div);
            });
            
            totalEl.innerText = formatMoney(total);
        };

        // UI Interactions
        window.toggleCart = () => {
            const overlay = document.getElementById('cart-overlay');
            const sidebar = document.getElementById('cart-sidebar');
            
            if (overlay.classList.contains('hidden')) {
                overlay.classList.remove('hidden');
                // Trigger reflow
                void overlay.offsetWidth;
                overlay.classList.remove('opacity-0');
                sidebar.classList.remove('translate-x-full');
            } else {
                overlay.classList.add('opacity-0');
                sidebar.classList.add('translate-x-full');
                setTimeout(() => {
                    overlay.classList.add('hidden');
                }, 300);
            }
        };

        // Mobile Menu Toggle
        document.getElementById('mobile-menu-btn').addEventListener('click', () => {
            const menu = document.getElementById('mobile-menu');
            menu.classList.toggle('hidden');
        });

        // Sticky Navbar effect
        window.addEventListener('scroll', () => {
            const nav = document.getElementById('navbar');
            if (window.scrollY > 50) {
                nav.classList.add('shadow-lg', 'bg-dark');
                nav.classList.remove('bg-dark/90');
            } else {
                nav.classList.remove('shadow-lg', 'bg-dark');
                nav.classList.add('bg-dark/90');
            }
        });

        // Set min date for reservation to today
        const today = new Date().toISOString().split('T')[0];
        document.getElementById('res-date').setAttribute('min', today);

        // Custom Toast Notification Function (Replaces alert)
        window.showToast = (message, type = 'info') => {
            const container = document.getElementById('toast-container');
            const toast = document.createElement('div');
            
            let bgColor = type === 'success' ? 'bg-green-900 border-green-500 text-green-100' : 
                          type === 'error' ? 'bg-red-900 border-red-500 text-red-100' : 
                          'bg-dark-card border-gold text-gold';
                          
            let icon = type === 'success' ? 'fa-check-circle' : 
                       type === 'error' ? 'fa-exclamation-circle' : 
                       'fa-info-circle';

            toast.className = `flex items-center p-4 mb-2 rounded shadow-lg border-l-4 ${bgColor} transition-all duration-300 transform translate-x-full opacity-0`;
            toast.innerHTML = `
                <i class="fas ${icon} mr-3 text-lg"></i>
                <span class="text-sm font-medium">${message}</span>
            `;
            
            container.appendChild(toast);
            
            // Animate in
            setTimeout(() => {
                toast.classList.remove('translate-x-full', 'opacity-0');
            }, 10);
            
            // Remove after 3 seconds
            setTimeout(() => {
                toast.classList.add('translate-x-full', 'opacity-0');
                setTimeout(() => {
                    toast.remove();
                }, 300);
            }, 3000);
        };

        // Initialization
        renderMenu();
        updateCartUI();
    </script>
</body>
</html>
