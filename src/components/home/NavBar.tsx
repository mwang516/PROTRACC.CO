import Link from 'next/link';

export default function NavBar() {

  return (
    <header className="bg-gray-800 text-white fixed top-0 w-full z-50 shadow-md">
      <nav className="container mx-auto flex justify-between items-center px-4">
        <Link href="/" className="text-xl font-bold py-4 hover:text-blue-400 transition-colors duration-300">PROTRACC.CO</Link>
        <div className="flex">
          {/* About Link */}
          <Link href="/about" className="relative group py-4 px-6">
            <p className="relative z-10 text-white group-hover:text-gray-900 group-hover:font-bold transition-colors duration-300">
              About
            </p>
            <div className="absolute inset-0 bg-white scale-y-0 origin-top group-hover:scale-y-100 transition-transform duration-300 ease-in-out z-0"></div>
          </Link>
  
          {/* Demo Link */}
          <Link href="https://www.youtube.com/watch?v=lFdqfANIhVw&ab_channel=JoeLiang" className="relative group py-4 px-6">
            <p className="relative z-10 text-white group-hover:text-gray-900 group-hover:font-bold transition-colors duration-300">
            Demo 
            </p>
            <div className="absolute inset-0 bg-white scale-y-0 origin-top group-hover:scale-y-100 transition-transform duration-300 ease-in-out z-0"></div>
          </Link>
  
          {/* GitHub Link */}
          <Link href="https://github.com/joewang0430/posture-visioner" className="relative group py-4 px-6">
            <p className="relative z-10 text-white group-hover:text-gray-900 group-hover:font-bold transition-colors duration-300">
            GitHub 
            </p>
            <div className="absolute inset-0 bg-white scale-y-0 origin-top group-hover:scale-y-100 transition-transform duration-300 ease-in-out z-0"></div>
          </Link>
        </div>
      </nav>
    </header>
  );
}