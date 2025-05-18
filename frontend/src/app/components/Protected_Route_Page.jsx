'use client'

import { useEffect, useState } from 'react'
import axios from 'axios'
import { useRouter } from 'next/navigation'

const Protected_Route_Page = () => {
  const [user, setUser] = useState(null)
  const router = useRouter()

  useEffect(() => {
    const token = localStorage.getItem('token')
    if (!token) {
      router.push('/')
      return
    }

    axios.get('http://localhost:8000/login/get-user', {
      headers: {
        Authorization: `Bearer ${token}`,
      },
    })
      .then(res => setUser(res.data))
      .catch(() => router.push('/'))
  }, [])

  const handleLogout = () => {
    localStorage.removeItem('token')
    router.push('/')
  }

  if (!user) {
    return (
      <div className="flex items-center justify-center h-screen bg-gray-100">
        <div className="text-lg font-semibold text-gray-700">Loading...</div>
      </div>
    )
  }

  return (
    <div className="flex items-center justify-center h-screen bg-gradient-to-br from-blue-100 via-purple-100 to-pink-100">
      <div className="bg-white shadow-xl rounded-2xl p-8 max-w-md text-center">
        <h1 className="text-3xl font-bold text-gray-800 mb-4">Welcome, <span className="text-blue-500">{user.username}</span>!</h1>
        <p className="text-gray-600 mb-6">
          You have successfully accessed the protected page.
        </p>
        <button
          onClick={handleLogout}
          className="px-6 py-2 cursor-pointer bg-red-500 hover:bg-red-600 text-white font-semibold rounded-full transition duration-200"
        >
          Logout
        </button>
      </div>
    </div>
  )
}

export default Protected_Route_Page
