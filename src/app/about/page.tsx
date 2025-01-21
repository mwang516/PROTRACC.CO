import NavBar from '../../components/home/NavBar';
import "../../app/globals.css";

export default function AboutPage() {
    return (
        <div className="min-h-screen">
            <div className="gradient"></div>
            <NavBar />
            <main className="max-w-4xl mx-auto px-6 py-8 mt-14">
                <h1 className="text-4xl font-bold mb-8">About</h1>
                
                <section className="mb-12">
                    <h2 className="text-2xl font-bold mb-4">Inspiration</h2>
                    <p className="text-lg leading-relaxed mb-6">
                        Do you want to run faster? Do you want to jump higher? For every aspiring athlete, 
                        biomechanics is the secret to improvement in performance. Weightlifting doesn&apos;t do 
                        it all -- a fast boat with no direction is lost. <span className="font-bold">PROTRACC.CO</span> revolutionizes the 
                        field of biomechanical analysis. No longer do you have to pay with an arm and a leg 
                        for some equipment, no longer do you have to wait impatiently for the gruesome 
                        instructions of some old coach. <span className="font-bold">PROTRACC.CO</span> lets you see where you have gone wrong, 
                        and decide for yourself.
                    </p>
                </section>

                <section className="mb-12">
                    <h2 className="text-2xl font-bold mb-4">What it does</h2>
                    <p className="text-lg leading-relaxed mb-6">
                        Our project is a web-based platform that allows users to upload videos of themselves 
                        performing a movement, from a golf swing to a simple vertical jump. The platform then 
                        uses machine learning algorithms to track the user&apos;s joints and generate a 3D 
                        visualization of their movement. This visualization can be compared to ideal movements, 
                        and users can receive feedback on their technique and suggestions for improvement.
                    </p>
                </section>

                <section className="mb-12">
                    <h2 className="text-2xl font-bold mb-4">How we built it</h2>
                    <p className="text-lg leading-relaxed mb-6">
                        The backend consisted of Mediapipe, OpenCV, and Flask to triangulate the Cartesian 
                        coordinates of the movements. The front end involved Three.js to visualize and interact 
                        with the 3D visualizations and React to create the webpages. We also used MongoDB to 
                        store user data and video files.
                    </p>
                </section>

                <section className="mb-12">
                    <h2 className="text-2xl font-bold mb-4">Startup</h2>
                    <p className="text-lg leading-relaxed mb-6">
                        In this market, <span className="font-bold">PROTRACC.CO</span> addresses a critical pain point: access to affordable, 
                        accurate, and actionable biomechanics analysis. Current solutions are often limited 
                        to high-end sports teams or elite athletes, with prices ranging from $5,000 to $50,000 
                        per year. Meanwhile, individual athletes and fitness enthusiasts are left with limited 
                        options, relying on trial-and-error methods or expensive personal coaching. <span className="font-bold">PROTRACC.CO</span> 
                        democratizes biomechanics analysis, making it accessible to anyone with a smartphone 
                        and an internet connection.
                    </p>
                </section>

                <section className="mb-12">
                    <h2 className="text-2xl font-bold mb-4">What&apos;s next for <span className="font-bold">PROTRACC.CO</span></h2>
                    <p className="text-lg leading-relaxed mb-6">
                        Of course, there are other features to consider about the product as well. A sense of 
                        depth is difficult with a single view—Humans have two eyes for a reason. That is why 
                        the next move for <span className="font-bold">PROTRACC.CO</span> is to integrate a second camera view. In fact, this has 
                        already been in production -- by placing two cameras in perpendicular angles of the 
                        scene, the cameras can effectively triangulate the coordinates of the subject. From 
                        prototyping, we found that having such a feature skyrockets in accuracy: there are now 
                        rarely blind spots, and the visualization seems to come to life.
                    </p>
                    <p className="text-lg leading-relaxed mb-6">
                        Furthermore, we aim to analyze and compare the user&apos;s biomechanics with the best 
                        athletes to reflect pointers that will work the best for them.
                    </p>
                </section>
            </main>
        </div>
    )
}