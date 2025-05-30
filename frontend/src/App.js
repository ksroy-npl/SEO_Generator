import React, { useState } from "react";
import axios from "axios";
import {
  Container,
  Box,
  Typography,
  TextField,
  Button,
  Paper,
  CircularProgress,
  Divider,
  Chip,
} from "@mui/material";

const accentColor = "#bfa980";

function App() {
  const [form, setForm] = useState({
    handle: "",
    title: "",
    body: "",
    brand_tone: ""
  });
  const [loading, setLoading] = useState(false);
  const [result, setResult] = useState(null);

  const handleChange = e => {
    setForm({ ...form, [e.target.name]: e.target.value });
  };

  const handleSubmit = async e => {
    e.preventDefault();
    setLoading(true);
    setResult(null);
    const formData = new FormData();
    Object.entries(form).forEach(([k, v]) => formData.append(k, v));
    try {
      const res = await axios.post("http://localhost:8000/generate-seo", formData);
      setResult(res.data.result);
    } catch (err) {
      alert("Error generating SEO description.");
    }
    setLoading(false);
  };

  return (
    <Box sx={{ background: "#faf9f6", minHeight: "100vh", py: 6 }}>
      <Container maxWidth="sm">
        <Paper elevation={4} sx={{ p: 4, borderRadius: 4 }}>
          <Typography
            variant="h4"
            align="center"
            sx={{
              fontFamily: "Playfair Display, serif",
              fontWeight: 700,
              color: "#222",
              letterSpacing: 1,
              mb: 2
            }}
          >
            SEO Product Description Generator
          </Typography>
          <Divider sx={{ mb: 3 }}>
            <Chip label="Nexus Point Luxe Style" sx={{ bgcolor: accentColor, color: "#fff" }} />
          </Divider>
          <form onSubmit={handleSubmit}>
            <TextField
              label="Handle"
              name="handle"
              value={form.handle}
              onChange={handleChange}
              required
              fullWidth
              margin="normal"
              variant="outlined"
            />
            <TextField
              label="Title"
              name="title"
              value={form.title}
              onChange={handleChange}
              required
              fullWidth
              margin="normal"
              variant="outlined"
            />
            <TextField
              label="Body"
              name="body"
              value={form.body}
              onChange={handleChange}
              required
              fullWidth
              margin="normal"
              variant="outlined"
              multiline
              minRows={3}
            />
            <TextField
              label="Brand Tone (optional)"
              name="brand_tone"
              value={form.brand_tone}
              onChange={handleChange}
              fullWidth
              margin="normal"
              variant="outlined"
            />
            <Button
              type="submit"
              variant="contained"
              fullWidth
              sx={{
                mt: 2,
                bgcolor: accentColor,
                color: "#fff",
                fontWeight: "bold",
                fontSize: 18,
                borderRadius: 2,
                py: 1.5,
                "&:hover": { bgcolor: "#a88e5a" }
              }}
              disabled={loading}
              endIcon={loading && <CircularProgress size={24} color="inherit" />}
            >
              {loading ? "Generating..." : "Generate SEO Description"}
            </Button>
          </form>
          {result && (
            <Paper
              elevation={2}
              sx={{
                mt: 5,
                p: 3,
                background: "#fffbe9",
                borderRadius: 3,
                border: `1px solid ${accentColor}`,
                boxShadow: "0 2px 12px #e8e1d2"
              }}
            >
              <Typography variant="h6" sx={{ fontWeight: 700, color: accentColor }}>
                Optimized Output
              </Typography>
              <Divider sx={{ my: 1 }} />
              <Typography variant="subtitle1" sx={{ fontWeight: 600, mt: 2 }}>
                Optimized Title:
              </Typography>
              <Typography sx={{ mb: 2 }}>{result.optimized_title}</Typography>
              <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                Optimized Body:
              </Typography>
              <Box
                sx={{
                  background: "#fff",
                  p: 2,
                  borderRadius: 2,
                  border: "1px solid #eee",
                  fontFamily: "inherit",
                  fontSize: 16,
                  mt: 1,
                  mb: 2,
                  color: "#222"
                }}
              >
                {result.optimized_body}
              </Box>
              <Typography variant="subtitle1" sx={{ fontWeight: 600 }}>
                Keywords Used:
              </Typography>
              <Typography>{result.keywords_used}</Typography>
            </Paper>
          )}
        </Paper>
        <Typography
          align="center"
          sx={{
            mt: 6,
            color: "#bfa980",
            fontFamily: "Playfair Display, serif",
            fontSize: 18,
            letterSpacing: 1
          }}
        >
          Powered by Gemini AI & Shopify SEO
        </Typography>
      </Container>
    </Box>
  );
}

export default App;
